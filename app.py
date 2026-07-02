import streamlit as st
from planner import allocate_time, generate_timetable

st.set_page_config(
    page_title="Agentic AI Study Planner",
    page_icon="📚",
    layout="wide"
)

st.title("🤖 Agentic AI Study Planner")
st.write("Generate an intelligent study timetable based on subject difficulty.")

# ---------------- Student Details ----------------

st.header("👨‍🎓 Student Information")

name = st.text_input("Student Name")
roll = st.text_input("Roll Number")
department = st.text_input("Department")

st.divider()

# ---------------- Planner ----------------

st.header("📚 Study Planner")

num_subjects = st.number_input(
    "Number of Subjects",
    min_value=1,
    max_value=10,
    value=5
)

subjects = []
difficulties = []

for i in range(num_subjects):

    col1, col2 = st.columns(2)

    with col1:
        subject = st.text_input(
            f"Subject {i+1}",
            key=f"sub{i}"
        )

    with col2:
        difficulty = st.selectbox(
            f"Difficulty {i+1}",
            ["Easy", "Medium", "Hard"],
            key=f"diff{i}"
        )

    subjects.append(subject)
    difficulties.append(difficulty)

hours = st.slider(
    "Study Hours Per Day",
    1,
    12,
    4
)

exam_date = st.date_input("Exam Date")

# ---------------- Generate ----------------

if st.button("🚀 Generate AI Study Plan"):

    if name == "":
        st.error("Please enter your name.")

    elif "" in subjects:
        st.error("Please enter all subject names.")

    else:

        plan = allocate_time(subjects, difficulties, hours)

        timetable = generate_timetable(plan)

        st.success("Study Plan Generated Successfully!")

        st.header("📊 Study Plan")

        for item in plan:

            st.write(
                f"**{item['subject']}** ({item['time']})"
            )

        st.header("🕒 Daily Timetable")

        for item in timetable:

            st.write(
                f"{item['start']} - {item['end']}   📘 {item['subject']}"
            )

        st.header("🤖 AI Suggestions")

        hard_subjects = [
            s for s, d in zip(subjects, difficulties)
            if d == "Hard"
        ]

        if hard_subjects:
            st.info(
                f"Focus first on: {', '.join(hard_subjects)}"
            )

        st.info("Take a 10-minute break after every study session.")
        st.info("Revise today's topics before sleeping.")

        st.progress(0.0)