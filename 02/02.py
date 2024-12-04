# 1 Report per line
# All increase or decrease
# at least 1, at most 3


file = "02/red_nose_reactor_reports.txt"
reports = [[int(x) for x in line.split(" ")] for line in open(file, "r")]


def is_successful(report: list) -> int:
    i = 0
    delta = report[i + 1] - report[i]
    while abs(delta) <= 3:
        i += 1
        try:
            new_delta = report[i + 1] - report[i]
            if delta * new_delta <= 0:
                return 0
            delta = new_delta
        except IndexError:
            return 1
    return 0


# Report
qt_safe_reports = 0
for report in reports:
    qt_safe_reports += is_successful(report)

unsafes = [report for report in reports if is_successful(report) == 0]

tolerable = 0
for unsafe in unsafes:
    for i in range(len(unsafe)):
        if is_successful(unsafe[:i] + unsafe[i + 1:]) == 1:
            tolerable += 1
            break

print(f"Successful reports: {qt_safe_reports}")
print(f"Tolerable successful reports: {qt_safe_reports + tolerable}")
