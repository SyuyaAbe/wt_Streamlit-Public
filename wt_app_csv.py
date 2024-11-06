import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='ワートリ')
st.title('ワートリ 隊員パラメータ')

# CSVファイルを読み込み
df = pd.read_csv('./params.csv')

# 名前のプルダウンメニューを作成
name = st.selectbox('キャラクターを選択してください', df['name'].unique())

# 選択された名前のデータを抽出
selected_data = df[df['名前'] == name]

# レーダーチャートを描画
if not selected_data.empty:
    st.markdown(f'## {name} のパラメータ')
    radar_data = selected_data[['トリオン', '防御・援護', '機動', '技術', '射程', '指揮', '特殊戦術']]
    radar_data = radar_data.T.reset_index()
    radar_data.columns = ['parameter', 'value']

    fig = px.line_polar(radar_data, r='value', theta='parameter', line_close=True)
    fig.update_traces(fill='toself')
    st.plotly_chart(fig)
