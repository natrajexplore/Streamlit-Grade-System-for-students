import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Fantasy Student Grade System",
    page_icon="🏆",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(-45deg,#141E30,#243B55,#4A00E0,#8E2DE2);
background-size:400% 400%;
animation: gradient 15s ease infinite;
color:white;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

.main-card{
background: rgba(255,255,255,0.12);
padding:25px;
border-radius:20px;
backdrop-filter: blur(10px);
box-shadow:0px 8px 30px rgba(0,0,0,.4);
}

.big-font{
font-size:45px;
font-weight:bold;
text-align:center;
color:#FFD700;
}

.small-font{
font-size:18px;
text-align:center;
color:white;
}

.metric{
font-size:25px;
color:#00FFB3;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown("<div class='big-font'>🏰 Fantasy Student Grade Portal</div>", unsafe_allow_html=True)
st.markdown("<div class='small-font'>✨ Academic Performance Dashboard ✨</div>", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Student Details
# -----------------------------
with st.container():
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)

    col1,col2=st.columns(2)

    with col1:
        name=st.text_input("👤 Student Name")
        roll=st.text_input("🆔 Roll Number")

    with col2:
        department=st.selectbox(
            "🎓 Department",
            ["Computer Science","IT","ECE","EEE","Mechanical","Civil"]
        )

    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Marks Entry
# -----------------------------
st.header("📚 Enter Subject Marks")

subjects=[
"Python",
"Mathematics",
"Database",
"Networking",
"Artificial Intelligence"
]

marks=[]

cols=st.columns(5)

for i,sub in enumerate(subjects):
    with cols[i]:
        value=st.number_input(
            sub,
            min_value=0,
            max_value=100,
            value=80,
            key=sub
        )
        marks.append(value)

# -----------------------------
# Calculate
# -----------------------------
if st.button("🚀 Generate Result"):

    total=sum(marks)
    percentage=total/5

    if percentage>=90:
        grade="A"
        performance="🌟 Outstanding"
        color="green"

    elif percentage>=80:
        grade="B"
        performance="🎯 Excellent"
        color="blue"

    elif percentage>=70:
        grade="C"
        performance="👍 Good"
        color="orange"

    elif percentage>=60:
        grade="D"
        performance="🙂 Average"
        color="gold"

    else:
        grade="E"
        performance="❌ Needs Improvement"
        color="red"

    if grade=="A":
        st.balloons()

    st.divider()

    c1,c2,c3,c4=st.columns(4)

    c1.metric("📖 Total",total)
    c2.metric("📊 Percentage",f"{percentage:.2f}%")
    c3.metric("🏆 Grade",grade)
    c4.metric("⭐ Performance",performance)

    st.write("")

    st.subheader("📈 Overall Progress")

    st.progress(int(percentage))

    st.write("")

    df=pd.DataFrame({
        "Subject":subjects,
        "Marks":marks
    })

    col1,col2=st.columns(2)

    with col1:

        fig=px.bar(
            df,
            x="Subject",
            y="Marks",
            color="Marks",
            text="Marks",
            title="Subject Performance"
        )

        fig.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig,use_container_width=True)

    with col2:

        fig2=px.pie(
            df,
            values="Marks",
            names="Subject",
            hole=.55,
            title="Marks Distribution"
        )

        fig2.update_layout(
            template="plotly_dark"
        )

        st.plotly_chart(fig2,use_container_width=True)

    st.subheader("📋 Result Summary")

    result=pd.DataFrame({
        "Subject":subjects,
        "Marks":marks
    })

    st.dataframe(result,use_container_width=True)

    csv=result.to_csv(index=False).encode()

    st.download_button(
        "💾 Download Result",
        csv,
        file_name=f"{name}_Result.csv",
        mime="text/csv"
    )

    st.success(f"🎉 Congratulations {name}! Your Grade is {grade}")


