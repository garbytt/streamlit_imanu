import streamlit as st
import time
from settings import API_KEY

st.write("API_KEY: ", API_KEY)

st.title("Hello World!!!!!!")

st.write("progress bar")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)
'done!'

st.sidebar.write("Interactive Widgets")

left_column, right_column = st.columns(2)
button = left_column.button("Click me!")
if button:
    right_column.write("Why hello there")
else:
    right_column.write("Goodbye")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を開く")
expander.write("問い合わせ内容を開く")
expander.write("問い合わせ内容を開く")
expander.write("問い合わせ内容を開く")


option = st.sidebar.text_input("Enter your name")
st.write(f"Hello {option}!")

condition = st.sidebar.slider("Select a value", min_value=0, max_value=100, value=100, step=1)
st.write(f"Condition: {condition}")


# option = st.selectbox(
#     "あなたはどのような人ですか？",
#     ("学生", "会社員", "自営業", "その他")
# )

# st.write(f"あなたは{option}です。")

# if st.checkbox("Show potato"):
#     image = Image.open("EVdrGOqU0AUJ5HW.jpg")
#     st.image(image, caption="potato", use_container_width=True)



# df = pd.DataFrame({
#     "first column": [1, 2, 3, 4],
#     "second column": [10, 20, 30, 40]
# })
# df = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )
# df = pd.DataFrame(
#     np.random.randn(100, 2)/[50, 50]+[35.69, 139.70],
#     columns=['lat', 'lon']
# )


# st.map(df)
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# st.table(df)
# st.dataframe(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """







