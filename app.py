import streamlit as st
import matplotlib.pyplot as plt
from processor.processor import DataProcessor
from reader.read_csv import ReadCSV

df  = ReadCSV('data/babynamesIL.csv').read()
proc = DataProcessor(df)

st.title('📊 ניתוח שמות בישראל (1948-2023) ')


st.header('🔹 דשבורד 1 - סך כל הכמות לשם')
name_input = st.text_input(':הכנס שם', key='name1')

if name_input:
    total_count = proc.sum_of_value('name', name_input, 'n')
    st.write(f'כמות האנשים עם השם{name_input}:\n'
             f' {total_count}')

st.header('🔹 דשבורד 2 - חלוקה לפי מגדר')
name_input2 = st.text_input(':הכנס שם', key='name2')

if name_input2:
    grouped_counts = proc.sum_of_grouped_values(['sex'], 'name', name_input2, 'n')
    st.write(grouped_counts)


st.header("🔹 דשבורד 3 - גרף לפי שנים ומגדר")
name_input3 = st.text_input(':הכנס שם', key='name3')
if name_input3:
    grouped_counts_year = proc.sum_of_grouped_values(['year','sex'],
                                                     'name', name_input3,
                                                     'n')

    fig , ax = plt.subplots()
    for gender in grouped_counts_year["sex"].unique():
        subset = grouped_counts_year[grouped_counts_year["sex"] == gender]
        ax.plot(subset["year"], subset["n"], label=gender)
    ax.set_xlabel("הנש")
    ax.set_ylabel("תומכ")
    title_text = f"שימוש בשם {name_input3} לפי שנים ומגדר"
    ax.set_title(title_text[::-1])
    ax.legend(title="רדגמ")
    st.pyplot(fig)