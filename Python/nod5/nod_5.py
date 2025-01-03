def part1_context_usage():
    try:
        try:
            result = 1 / 0
        except ZeroDivisionError:
            raise ValueError("ValueError raised after ZeroDivisionError")
    except ValueError as e:
        import traceback
        traceback.print_exc()


def part2_cause_usage():
    try:
        try:
            result = 1 / 0
        except ZeroDivisionError as ex:
            raise ValueError("ValueError caused by ZeroDivisionError") from ex 
    except ValueError as e:
        import traceback
        traceback.print_exc()


def part3_combined_context_and_cause():
    try:
        try:
            try:
                result = 1 / 0 
            except ZeroDivisionError:
                raise ValueError("ValueError raised after ZeroDivisionError")  # __context__ tiek automātiski pievienots
        except ValueError as e:
            raise RuntimeError("RuntimeError caused by ValueError") from e  # Izmantojam __cause__
    except RuntimeError as e:
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("Part 1: __context__")
    part1_context_usage()

    print("\nPart 2: __cause__")
    part2_cause_usage()

    print("\nPart 3: __context__ and __cause__")
    part3_combined_context_and_cause()
