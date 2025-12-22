import re
from datetime import datetime
from pathlib import Path

from main import CarDimensions, CarInfo


def folder_creations(
    parent_folder: Path, test_list, dimentions: CarDimensions, info: CarInfo
):
    folder_prefix = f"{info.year[-2:]}-{info.oem}-{info.number}"

    main_folder = parent_folder / f"{folder_prefix}-{info.model_name}"
    main_folder.mkdir(exist_ok=True, parents=True)

    for test in test_list:
        test_name = f"{info.number}"

        for items in test["_ui"]["columns"]:
            test_name = f"{test_name}-{sanitize_folder_name(items[1], '')}"

        test_folder = main_folder / f"{folder_prefix}-{test['macro_type']}" / test_name
        test_folder = create_unique_folder(test_folder)

        (test_folder / "Channel").mkdir(exist_ok=True, parents=True)
        (test_folder / "Movie").mkdir(exist_ok=True, parents=True)

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
    # Keep letters, numbers, spaces, dashes and underscores
    name = re.sub(r"[^a-zA-Z0-9_-]", replacement, name)
    return name.strip()


def mme_processor(test, dimentions: CarDimensions, info: CarInfo):
    output = [
        "Data format edition number:\t1.6",
        "Laboratory name:\tCSI S.p.A.",
        "Customer name:\tEuro NCAP",
    ]

    output.append("Customer project ref. number:\t" + info.number)
    output.append("Title:\t	Euro NCAP " + info.year)
    current_date = datetime.now().strftime("%Y/%m/%d,%H:%M")
    output.append("Timestamp:\t" + current_date)
    output.append("Scenario:\t" + test["name"])
    output.append("Type of the test:\t" + test["test_type"])
    test_condition = test["test_condition"]
    if test_condition == "N/A":
        test_condition = ""

    output.append("Condition of test:\t" + test["test_condition"])
    output.append("Region:\tEU")
    # todo robustness
    robustness = test["robustness_type"]
    if "robustness_layer" in test:
        robustness += ";" + test["robustness_layer"]
        if "robustness_parameter" in test:
            robustness += ";" + str(test["robustness_parameter"])

    output.append("Robustness Layer:\t" + robustness)
    output.append("Name of test object 1:\t" + info.model_name)
    output.append("Driver Position object 1:\t1")
    output.append("Ref. number of test object 1:\t" + info.vin)
    output.append("S/W version of TOB 1:\t" + info.sw_version)
    output.append(
        "Dimensions of test object 1:\t"
        + str(dimentions.length)
        + ","
        + str(dimentions.width)
    )

    front_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.front)
    front_profile = f"Shape Front TOB 1:\t{front_points_str}"

    output.append(front_profile)

    rear_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.back)
    rear_profile = f"Shape Rear TOB 1:\t{rear_points_str}"

    output.append(rear_profile)

    right_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.side)
    right_profile = f"Shape Right Side TOB 1:\t{right_points_str}"

    output.append(right_profile)

    left_points_str = ", ".join(f"({p.x};{p.y})" for p in dimentions.profile.side)
    left_profile = f"Shape Left Side TOB 1:\t{left_points_str}"

    output.append(left_profile)

    # TODO update the
    # speed
    # acceleration
    # overlap
    # relative to the robustness layer

    output.append("Velocity longitudinal TOB 1:\t" + str(test["long_speed_VUT"]))
    output.append("Velocity lateral TOB 1:\t" + str(test["lat_speed_VUT"]))

    output.append("Impact side TOB 1:\t" + str(test["lat_speed_VUT"]))
    output.append("Impact location of test object 1:\t" + str(test["overlap"]))

    output.append("Name of test object 2:\t" + test["target_type"])

    output.append("Velocity test object 2:\t" + str(test["target_speed"]))
    output.append("Acceleration test object 2:\t" + str(test["target_acceleration"]))

    output.append("Heading test object 2:\t" + str(test["target_heading"]))
    output.append("Type of data source:\tPhysical_Test")

    return output
