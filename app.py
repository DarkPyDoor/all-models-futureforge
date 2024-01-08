import streamlit as st
import requests
from streamlit import session_state as state

st.set_page_config(layout="wide")

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get('data', [])

def display_model_card(model, col):
    with col:
        st.markdown(f"### {model.get('name', 'Без названия')}")
        st.write(model.get('description', 'Описание отсутствует.'))
        st.markdown(f"**Длина контекста**: {model.get('context_length', 'Не указана')}")
        architecture = model.get('architecture', {})
        st.write(f"**Архитектура**: {architecture.get('instruct_type', 'Не указана')}")
        st.write(f"**Токенизатор**: {architecture.get('tokenizer', 'Не указан')}")
        pricing = model.get('pricing', {})
        st.write(f"**Цена за completion**: {pricing.get('completion', 'Не указана')}")
        st.write(f"**Цена за prompt**: {pricing.get('prompt', 'Не указана')}")
        st.write(f"**ID модели**: {model.get('id', 'Не указан')}")
        st.write("---")

if 'welcome_message_shown' not in state:
    st.warning('Добро пожаловать на сайт FutureForge!')
    state.welcome_message_shown = True

st.sidebar.title("Меню")
st.sidebar.markdown("[Владелец](https://t.me/botorotss2)")
st.sidebar.markdown("[Телеграм Канал](https://t.me/futureforge_channel)")
st.sidebar.markdown("[Основной бот](https://t.me/futureforgedev_bot)")
st.sidebar.markdown("[Сайт](https://www.futureforge.dev)")
st.sidebar.markdown("[API](https://api.futureforge.dev/docs)")
st.sidebar.markdown("[Панель](https://panel.futureforge.dev)")
st.sidebar.markdown("[Донат](https://t.me/futureforge_channel/165)")

def main():
    st.title("Список моделей с OpenRouter AI")

    url = 'https://openrouter.ai/api/v1/models'

    try:
        models_data = fetch_data(url)
        cols = st.columns(3)
        for idx, model in enumerate(models_data):
            display_model_card(model, cols[idx % 3])
    except requests.HTTPError as http_err:
        st.error(f"Произошла ошибка HTTP при получении данных: {http_err}")
    except Exception as e:
        st.error(f"Произошла ошибка при получении данных: {e}")

if __name__ == "__main__":
    main()
