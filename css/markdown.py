def load_button_css():
    return """
    <style>
    /* ===== 全局按钮基础样式 ===== */
    div.stButton > button {
        height: 70px;
        width: 220px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 12px;

        /* ⭐ 关键：强制黑色外框 */
        border: 2px solid black !important;
        outline: none !important;

        transition: all 0.15s ease-in-out;
    }

    /* ===== 去掉 Streamlit 默认阴影（很重要） ===== */
    div.stButton > button {
        box-shadow: none !important;
    }

    /* ===== START ===== */
    div.stButton > button.start-btn {
        background-color: #28a745;
        color: white;
        border: 2px solid black !important;
    }

    div.stButton > button.start-btn:hover {
        background-color: #2ecc71;
        border: 2px solid black !important;
    }

    div.stButton > button.start-btn:active {
        transform: scale(0.97);
        border: 2px solid black !important;
    }

    /* ===== STOP ===== */
    div.stButton > button.stop-btn {
        background-color: #dc3545;
        color: white;
        border: 2px solid black !important;
    }

    div.stButton > button.stop-btn:hover {
        border: 2px solid black !important;
    }

    div.stButton > button.stop-btn:active {
        transform: scale(0.97);
        border: 2px solid black !important;
    }

    </style>
    """