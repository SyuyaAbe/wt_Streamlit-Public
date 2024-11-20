import streamlit as st
import pandas as pd
import plotly.express as px
#import streamlit.components.v1 as components


st.set_page_config(page_title='ワートリ', layout="wide")

st.title('ワールドトリガー キャラクター別パラメータ&トリガー構成')


# CSVファイルを読み込み
df = pd.read_csv('./params.csv')
equipment_df = pd.read_csv('./equipment.csv')


# 'name'列が存在しない場合、日本語列名である可能性を考慮
name_column = '名前' if '名前' in df.columns else 'name'
# 名前のプルダウンメニューを作成
name = st.selectbox('キャラクターを選択してください', df[name_column].unique())


# 選択された名前のデータを抽出
selected_data = df[df['名前'] == name]

# レーダーチャートを描画
if not selected_data.empty:
    st.markdown(f'## {name} のパラメータ')
    radar_data = selected_data[['トリオン','攻撃','防御・援護','機動','技術','射程','指揮','特殊戦術']]
    radar_data = radar_data.T.reset_index()
    radar_data.columns = ['parameter', 'value']

    # レーダーチャートの作成
    fig = px.line_polar(radar_data, r='value', theta='parameter', line_close=True)
    fig.update_traces(fill='toself', marker=dict(color='#b3e5fc'))
    fig.update_layout(
        polar=dict(
        bgcolor="white",
        radialaxis=dict(tickfont=dict(color='red'))  # メモリの数字の色を設定
        )
    )
    st.plotly_chart(fig)


    # トリガー構成の表示
    st.markdown(f'## {name} のトリガー構成')
    
    # 選択したキャラクターのトリガー構成を抽出
    selected_equipment = equipment_df[equipment_df['名前'] == name]
    selected_data = df[df['名前'] == name]

    if name == "木崎レイジ":
        # 特定の表示方法: 木崎レイジ
        trigger_data = selected_equipment[['メイントリガー1', 'メイントリガー2', 'メイントリガー3', 'メイントリガー4','メイントリガー5', 'メイントリガー6', 'メイントリガー7',
                                           'サブトリガー1', 'サブトリガー2', 'サブトリガー3', 'サブトリガー4', 'サブトリガー5', 'サブトリガー6', 'サブトリガー7']]
        st.table(trigger_data)
    else:
        # 他のキャラクターのトリガー構成を表示
        trigger_data = selected_equipment[['メイントリガー1', 'メイントリガー2', 'メイントリガー3', 'メイントリガー4',
                                           'サブトリガー1', 'サブトリガー2', 'サブトリガー3', 'サブトリガー4']]
        st.table(trigger_data)
