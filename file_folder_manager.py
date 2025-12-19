from datetime import datetime
from pathlib import Path

from main import CarDimensions, CarInfo


def folder_creations(
    parent_folder: Path, test_list, dimentions: CarDimensions, info: CarInfo
):
    main_folder = parent_folder / "Test"
    main_folder.mkdir(exist_ok=True)

    idx = 0

    for test in test_list:
        test_folder = main_folder / str(idx)
        test_folder.mkdir(exist_ok=True)
        (test_folder / "Channel").mkdir(exist_ok=True)
        (test_folder / "Movie").mkdir(exist_ok=True)

        mme_file_lines = mme_processor(test, dimentions, info)

        with open(test_folder / (str(idx) + ".mme"), "w", encoding="utf-8") as file:
            for line in mme_file_lines:
                file.write(line + "\n")

        idx += 1


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
    output.append("Robustness Layer:\t")
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

    # TODO update the speed relative to the robustness layer

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
