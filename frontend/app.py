
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Laptop Price Predictor")
st.write(
    "Enter laptop specifications to estimate its price "
    "using Machine Learning."
)

# Fetch valid categorical options from FastAPI
@st.cache_data(ttl=3600)
def get_options():
    response = requests.get(
        f"{API_URL}/options",
        timeout=10
    )
    response.raise_for_status()
    return response.json()


try:
    options = get_options()
except requests.RequestException:
    st.error(
        "Cannot connect to FastAPI. "
        "Make sure the backend is running "
        "and the /options endpoint is available."
    )
    st.stop()


with st.form("laptop_form"):

    st.subheader("Laptop Specifications")

    company = st.selectbox(
        "Company", options["company"]
    )

    typename = st.selectbox(
        "Laptop Type", options["typename"]
    )

    cpu = st.selectbox(
        "Processor", options["cpu"]
    )

    gpu_brand = st.selectbox(
        "GPU Brand", options["gpu_brand"]
    )

    os = st.selectbox(
        "Operating System", options["os"]
    )

    ram = st.selectbox(
        "RAM (GB)", [2, 4, 8, 16, 32, 64]
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.1,
        max_value=10.0,
        value=1.8,
        step=0.1
    )

    st.subheader("Display")

    screen_size = st.number_input(
        "Screen Size (inches)",
        min_value=5.0,
        max_value=25.0,
        value=15.6
    )

    resolution = st.selectbox(
        "Screen Resolution",
        [
            "1366x768",
            "1920x1080",
            "2560x1440",
            "3840x2160"
        ]
    )

    touchscreen = st.checkbox("Touchscreen")
    ips_panel = st.checkbox("IPS Panel")

    st.subheader("Storage")

    hdd = st.number_input(
        "HDD (GB)", min_value=0,
        value=0, step=128
    )

    ssd = st.number_input(
        "SSD (GB)", min_value=0,
        value=256, step=128
    )

    hybrid = st.number_input(
        "Hybrid Storage (GB)",
        min_value=0, value=0, step=128
    )

    flash_drive = st.number_input(
        "Flash Storage (GB)",
        min_value=0, value=0, step=32
    )

    submitted = st.form_submit_button(
        "Predict Laptop Price",
        use_container_width=True
    )


if submitted:

    width, height = map(int, resolution.split("x"))

    payload = {
        "company": company,
        "typename": typename,
        "cpu": cpu,
        "ram": ram,
        "os": os,
        "weight": weight,
        "touchscreen": touchscreen,
        "ips_panel": ips_panel,
        "screen_size": screen_size,
        "resolution_width": width,
        "resolution_height": height,
        "hdd": hdd,
        "ssd": ssd,
        "hybrid": hybrid,
        "flash_drive": flash_drive,
        "gpu_brand": gpu_brand
    }

    try:
        with st.spinner("Predicting laptop price..."):
            response = requests.post(
                f"{API_URL}/predict",
                json=payload,
                timeout=30
            )
            response.raise_for_status()

            result = response.json()
            price = result["predicted_price"]
            currency = result["currency"]

        st.success("Prediction completed!")

        if currency == "INR":
            st.metric(
                "Estimated Laptop Price",
                f"₹{price:,.2f}"
            )
        else:
            st.metric(
                "Estimated Laptop Price",
                f"{price:,.2f} {currency}"
            )

        st.caption(
            "This is an ML-based estimate, "
            "not a guaranteed market price."
        )

    except requests.RequestException as e:
        st.error(f"Prediction request failed: {e}")
