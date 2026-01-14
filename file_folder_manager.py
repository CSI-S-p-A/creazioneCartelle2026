import re
from datetime import datetime
from pathlib import Path

from main import CarDimensions, CarInfo


def folder_creations(
    parent_folder: Path, test_list, dimentions: CarDimensions, info: CarInfo
):
    # Construct the prefix with the main information
    folder_prefix = f"{info.year[-2:]}-{info.oem}-{info.number}"

    main_folder = parent_folder / f"{folder_prefix}-{info.make}_{info.model}"
    main_folder.mkdir(exist_ok=True, parents=True)

    for test in test_list:
        test_name = f"{info.number}"

        # Construct the folder name from the info that are displayed in the QTable
        # assuming they are the important ones
        for item in test["_ui"]["columns"]:
            if item[1] == "N/A":
                continue

            test_name = f"{test_name}-{sanitize_folder_name(item[1], '')}"

        # Creating all the folders
        test_folder = main_folder / f"{folder_prefix}-{test['macro_type']}" / test_name
        test_folder = create_unique_folder(test_folder)

        (test_folder / "Channel").mkdir(exist_ok=True, parents=True)
        (test_folder / "Movie").mkdir(exist_ok=True, parents=True)

        # Generating and creating the mme file
        mme_file_lines = mme_processor(test, dimentions, info)

        with open(test_folder / (f"{test_name}.mme"), "w", encoding="utf-8") as file:
            for line in mme_file_lines:
                file.write(line + "\n")


def create_unique_folder(folder_name: Path) -> Path:
    if not folder_name.exists():
        folder_name.mkdir(parents=True)
        return folder_name

    counter = 2

    while True:
        new_path = folder_name.with_name(f"{folder_name.name}_{counter}")
        if not new_path.exists():
            new_path.mkdir(parents=True)
            return new_path

        counter += 1


def sanitize_folder_name(name: str, replacement="_") -> str:
    # Removes strange characters from the name that could lead to problems
    # when creating a folder
    name = re.sub(r"[^a-zA-Z0-9_-]", replacement, name)
    return name.strip()


def mme_processor(test, dimentions: CarDimensions, info: CarInfo):
    # TODO
    # the main thing missing right now is a way to have the
    # info about the target and the impact (like impact location)
    # to be removed just in the case of a NVT ELK OV, right now the only fast solution
    # would be to just include the "NVT" option to basically all the parameters in the
    # selection of the test.
    # Better approaches are for sure possibile but I dont have time to think and test
    # them.
    output = [
        "Data format edition number:\t1.6",
        "Laboratory name:\tCSI S.p.A.",
        "Customer name:\tEuro NCAP",
    ]

    output.append("Customer project ref. number:\t" + info.number)
    output.append("Title:\t	Euro NCAP " + info.year)
    current_date = datetime.now().strftime("%Y/%m/%d,%H:%M")
    output.append("Timestamp:\t" + current_date)

    # Doing test.get(.......) ensure that you at least have an output of "NOVALUE" if the data is for
    # some reason missing in the test dictionary
    output.append("Scenario:\t" + test.get("name", "NOVALUE"))
    output.append("Type of the test:\t" + test.get("test_type", "NOVALUE"))
    output.append("Subtype of the test:\t" + test.get("test_condition", "NOVALUE"))
    # TODO I've hardcoded the run repetition to be 1. I dont have an easy fix for this other
    # than adding another combobox in the test adder to specify the number (and this is still not that easy).
    output.append("Run repetition:\t1")
    output.append("Region:\tEU")

    robustness = test.get("robustness_type", "NOVALUE")
    robustness_layer = test.get("robustness_layer")
    if robustness_layer is not None:
        robustness += ";" + str(robustness_layer)

        robustness_parameter = test.get("robustness_parameter")
        if robustness_parameter is not None:
            robustness += ";" + str(robustness_parameter)

    output.append("Robustness Layer:\t" + robustness)

    tob1_name = f"{info.make}, {info.model}"
    output.append("Name TOB 1:\t" + tob1_name)

    output.append("Driver position TOB 1:\t1")
    output.append("Ref. number of TOB 1:\t" + info.vin)
    output.append("S/W version of TOB 1:\t" + info.sw_version)
    output.append(
        "Dimensions of TOB 1:\t" + str(dimentions.length) + "," + str(dimentions.width)
    )

    front_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.front)
    output.append(f"Shape Front TOB 1:\t{front_points_str}")

    left_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.side)
    output.append(f"Shape Left Side TOB 1:\t{left_points_str}")

    rear_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.back)
    output.append(f"Shape Rear TOB 1:\t{rear_points_str}")

    right_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.side)
    output.append(f"Shape Right Side TOB 1:\t{right_points_str}")

    output.append("Front overhang TOB 1:\t" + str(dimentions.overhang))
    output.append(
        "Velocity longitudinal TOB 1:\t" + str(test.get("long_speed_VUT", "NOVALUE"))
    )
    output.append(
        "Lane Departure Velocity TOB 1:\t" + str(test.get("lat_speed_VUT", "NOVALUE"))
    )

    output.append("Impact side TOB 1:\t" + str(test.get("lat_speed_VUT", "NOVALUE")))
    output.append("Impact location TOB 1:\t" + str(test.get("overlap", "NOVALUE")))

    output.append("Driver State TOB 1:\tNOVALUE")

    output.append("Name TOB 2:\t" + test.get("target_type", "NOVALUE"))
    output.append("Velocity TOB 2:\t" + str(test.get("target_speed", "NOVALUE")))
    output.append(
        "Acceleration TOB 2:\t" + str(test.get("target_acceleration", "NOVALUE"))
    )
    output.append("Heading TOB 2:\t" + str(test.get("target_heading", "NOVALUE")))

    output.append("Type of data source:\tPhysical Test")

    return output
