import streamlit as st
from src.models.helsinki.langchain_init import llmchain_init


lang_list = [
    {'key': 'en', 'val': 'English'},
    {'key': 'fr', 'val': 'French'},
    {'key': 'de', 'val': 'German'},
    {'key': 'it', 'val': 'Italian'},
    {'key': 'es', 'val': 'Spanish'},
    {'key': 'ar', 'val': 'Arabic'},
]



lang_alert = ''
chain = None
translation = ''

for item in lang_list:
    item['disabled'] = False

if 'lang_list' not in st.session_state:
    st.session_state['lang_list'] = lang_list
if 'selected_languages' not in st.session_state:
    st.session_state['selected_languages'] = []

def update_selection(item):
    selected_keys = [key for key in st.session_state if st.session_state[key] is True]
    st.session_state['selected_languages'] = [
        item for item in st.session_state['lang_list'] if item['key'] in selected_keys
    ]
    for item in st.session_state['lang_list']:
        item['disabled'] = (
            len(st.session_state['selected_languages']) >= 2
            and item not in st.session_state['selected_languages']
        )



st.sidebar.title('Caesar - AI Translator', anchor=False)
st.sidebar.divider()

st.sidebar.text('Available Languages')

st.title('Write anything and I shall translate it for you!', anchor=False)
st.divider()

dynamic_container = st.empty()

for item in st.session_state['lang_list']:
    st.sidebar.checkbox(
        item['val'],
        key=item['key'],
        disabled=item['disabled'],
        on_change=update_selection,
        args=[
            item,
    ],)


if len(st.session_state['selected_languages']) == 2:
    selected_vals = [item['val'] for item in st.session_state['selected_languages']]
    lang_alert = f"You've selected {len(selected_vals)} languages: {', '.join(selected_vals)}"
else:
    lang_alert = 'Please select exactly two languages.'

if len(st.session_state['selected_languages']) == 2:

    @st.cache_resource
    def get_chain(lang):
        return llmchain_init(lang)

    chain = get_chain([item['key'] for item in st.session_state['selected_languages']])

    with dynamic_container.container():
        input_col, output_col = st.columns(2)

        user_prompt = input_col.text_area("Enter your text here...")

        button = st.sidebar.button(
            'Translate', disabled=user_prompt.strip() == '', use_container_width=True
        )

        if button:
            if user_prompt.strip():
                try:
                    translation = chain.run(input=user_prompt)
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please enter something at least.")
        output_col.text_area("Translated text", translation)
else:
    dynamic_container.info(lang_alert)