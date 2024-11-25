import streamlit as st


def aplicar_estilos():
    estilo_css = """
    <style>
    body {
        background-color: #f0f4f8;
        font-family: 'Open Sans', sans-serif;
        color: #333;
        margin: 0;
        padding: 0;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto', sans-serif;
        color: #444;
        text-align: center;
    }

    a {
        color: #007bff;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    .stButton>button {
        background-color: #1a73e8;
        color: #fff;
        border-radius: 20px;
        padding: 12px 25px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s, transform 0.3s;
    }

    .stButton>button:hover {
        background-color: #185abc;
    }

    .stButton>button:active {
        background-color: #0f47a1;
        transform: scale(0.98);
    }

    .stTextInput>div>div>input {
        border: 2px solid #1a73e8;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        outline: none;
        transition: border-color 0.3s;
    }

    .stTextInput>div>div>input:focus {
        border-color: #0f47a1;
    }

    .stDataFrame {
        margin: auto;
        border: 2px solid #1a73e8;
        border-radius: 10px;
        overflow: hidden;
        width: 90%;
    }

    .stDownloadButton>button {
        background-color: #28a745;
        color: #fff;
        border-radius: 20px;
        padding: 12px 25px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s, transform 0.3s;
    }

    .stDownloadButton>button:hover {
        background-color: #218838;
    }

    .stDownloadButton>button:active {
        background-color: #1e7e34;
        transform: scale(0.98);
    }

    .stAlert>div {
        padding: 15px;
        border-radius: 10px;
        color: #fff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }

    .stAlert-warning>div {
        background-color: #ffc107;
        border-left: 5px solid #ffcd39;
    }

    .stAlert-success>div {
        background-color: #28a745;
        border-left: 5px solid #34d058;
    }

    .stAlert-error>div {
        background-color: #dc3545;
        border-left: 5px solid #e22d42;
    }

    .stContainer {
        padding: 20px;
        background: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    .stDataFrame table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
    }

    .stDataFrame th, .stDataFrame td {
        border: 1px solid #ddd;
        padding: 8px;
    }

    .stDataFrame th {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: center;
        background-color: #1a73e8;
        color: #fff;
    }

    header {
        background-color: #1a73e8;
        color: #fff;
        padding: 20px 0;
        text-align: center;
        border-radius: 0 0 20px 20px;
    }

    header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: normal;
    }

    .container {
        max-width: 1100px;
        margin: 20px auto;
        padding: 20px;
    }

    button {
      --border-color: linear-gradient(-45deg, #ffae00, #7e03aa, #00fffb);
      --border-width: 0.125em;
      --curve-size: 0.5em;
      --blur: 30px;
      --bg: #080312;
      --color: #afffff;
      color: var(--color);
      cursor: pointer;
      /* use position: relative; so that BG is only for .btn */
      position: relative;
      isolation: isolate;
      display: inline-grid;
      place-content: center;
      padding: 0.5em 1.5em;
      font-size: 17px;
      border: 0;
      text-transform: uppercase;
      box-shadow: 10px 10px 20px rgba(0, 0, 0, 0.6);
      clip-path: polygon(
        /* Top-left */ 0% var(--curve-size),
        var(--curve-size) 0,
        /* top-right */ 100% 0,
        100% calc(100% - var(--curve-size)),
        /* bottom-right 1 */ calc(100% - var(--curve-size)) 100%,
        /* bottom-right 2 */ 0 100%
      );
      transition: color 250ms;
    }
    
    button::after,
    button::before {
      content: "";
      position: absolute;
      inset: 0;
    }
    
    button::before {
      background: var(--border-color);
      background-size: 300% 300%;
      animation: move-bg7234 5s ease infinite;
      z-index: -2;
    }
    
    @keyframes move-bg7234 {
      0% {
        background-position: 31% 0%;
      }
    
      50% {
        background-position: 70% 100%;
      }
    
      100% {
        background-position: 31% 0%;
      }
    }
    
    button::after {
      background: var(--bg);
      z-index: -1;
      clip-path: polygon(
        /* Top-left */ var(--border-width)
          calc(var(--curve-size) + var(--border-width) * 0.5),
        calc(var(--curve-size) + var(--border-width) * 0.5) var(--border-width),
        /* top-right */ calc(100% - var(--border-width)) var(--border-width),
        calc(100% - var(--border-width))
          calc(100% - calc(var(--curve-size) + var(--border-width) * 0.5)),
        /* bottom-right 1 */
          calc(100% - calc(var(--curve-size) + var(--border-width) * 0.5))
          calc(100% - var(--border-width)),
        /* bottom-right 2 */ var(--border-width) calc(100% - var(--border-width))
      );
      transition: clip-path 500ms;
    }
    
    button:where(:hover, :focus)::after {
      clip-path: polygon(
        /* Top-left */ calc(100% - var(--border-width))
          calc(100% - calc(var(--curve-size) + var(--border-width) * 0.5)),
        calc(100% - var(--border-width)) var(--border-width),
        /* top-right */ calc(100% - var(--border-width)) var(--border-width),
        calc(100% - var(--border-width))
          calc(100% - calc(var(--curve-size) + var(--border-width) * 0.5)),
        /* bottom-right 1 */
          calc(100% - calc(var(--curve-size) + var(--border-width) * 0.5))
          calc(100% - var(--border-width)),
        /* bottom-right 2 */
          calc(100% - calc(var(--curve-size) + var(--border-width) * 0.5))
          calc(100% - var(--border-width))
      );
      transition: 200ms;
    }
    
    button:where(:hover, :focus) {
      color: #fff;
    }

    
    </style>
    """
    st.markdown(estilo_css, unsafe_allow_html=True)