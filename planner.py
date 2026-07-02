from datetime import datetime, timedelta


def allocate_time(subjects, difficulties, total_hours):

    total_minutes = total_hours * 60

    # Difficulty weights
    weight_map = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    weights = [weight_map[d] for d in difficulties]
    total_weight = sum(weights)

    study_plan = []

    for subject, weight in zip(subjects, weights):
        minutes = round((weight / total_weight) * total_minutes)

        hrs = minutes // 60
        mins = minutes % 60

        if hrs > 0 and mins > 0:
            time = f"{hrs} hr {mins} min"
        elif hrs > 0:
            time = f"{hrs} hr"
        else:
            time = f"{mins} min"

        study_plan.append({
            "subject": subject,
            "minutes": minutes,
            "time": time
        })

    return study_plan


def generate_timetable(plan):

    current_time = datetime.strptime("09:00", "%H:%M")

    timetable = []

    for item in plan:

        start = current_time

        end = start + timedelta(minutes=item["minutes"])

        timetable.append({
            "subject": item["subject"],
            "start": start.strftime("%I:%M %p"),
            "end": end.strftime("%I:%M %p")
        })

        current_time = end + timedelta(minutes=10)

    return timetable