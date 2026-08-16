import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="OrbitIQ", page_icon="🌊", layout="wide")

IMG_SIZE = 128
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# DARK THEME 
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    }
    .header-box {
        background: linear-gradient(90deg, rgba(0,212,255,0.1) 0%, rgba(9,9,121,0.1) 100%);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(0,212,255,0.3);
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }
    .dashboard-card {
        background: rgba(255,255,255,0.05);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 1rem;
    }
    .flood-alert {
        background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
        color:black;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 0 20px rgba(255,65,108,0.5);
    }
    .safe-box {
        background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%);
        color: black;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 0 20px rgba(0,176,155,0.5);
    }
    h1, h2, h3, p { color: white !important; }
</style>
""", unsafe_allow_html=True)

# HEADER - Pic 1 ka style
st.markdown("""
<div class="header-box">
    <h1 style='font-size: 48px;'>🌊 Flood Disaster Detection</h1>
    <p style='font-size: 18px; color: #a0d2eb;'>AI Powered Real-time Flood Analysis | OrbitIQ</p>
    <button style='background: #00d4ff; color: white; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold;'> Analyze Now</button>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = models.resnet18(weights=None)
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_ftrs, 128), nn.ReLU(), nn.Dropout(0.3),
        nn.Linear(128, 1), nn.Sigmoid()
    )
    model.load_state_dict(torch.load('flood_image_model.pth', map_location=DEVICE))
    model = model.to(DEVICE)
    model.eval()
    return model

model = load_model()

transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def predict(image):
    img_t = transform(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        output = model(img_t)
    prob = output.item()
    if prob < 0.5:
        return "FLOOD", (1 - prob) * 100, prob
    else:
        return "NO FLOOD", prob * 100, prob

# 3 COLUMN DASHBOARD - Pic 2 ka style
col1, col2, col3 = st.columns([1, 1.5, 1])

with col1:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("🎯 AI Prediction")
    if uploaded_file:
        label, confidence, raw_prob = predict(image)
        if label == "FLOOD":
            st.markdown(f'<div class="flood-alert">⚠️ FLOOD DETECTED</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="safe-box">✅ NO FLOOD</div>', unsafe_allow_html=True)
        st.metric("Confidence", f"{confidence:.2f}%")
        st.progress(confidence / 100)
    else:
        st.info("Upload image to analyze")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
    st.subheader("📊 Model Stats")
    st.metric("Accuracy", "94.07%")
    st.metric("Model", "ResNet18")
    st.metric("Status", "Live")
    st.markdown('</div>', unsafe_allow_html=True)

# GRAPHS SECTION
st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
st.subheader("📈 Analytics Dashboard")

g1, g2 = st.columns(2)

with g1:
    # Line Graph - Water Level Trend
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    water_level = [20, 35, 30, 50, 45, 70]
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=months, y=water_level, mode='lines+markers', 
                              line=dict(color='#00d4ff', width=3), name='Water Level'))
    fig1.update_layout(title="Water Level Trend",
                       font=dict(size=14, color='cyan') ,
                       template="plotly_dark", 
                       paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig1, use_container_width=True)

with g2:
        # Bar Graph - Risk Assessment
        areas = ['Area A', 'Area B', 'Area C', 'Area D']
        risk = [30, 80, 45, 60]
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(x=areas, y=risk, marker_color=['#96c93d','#ff416c','#00d4ff','#ff4b2b']))
        fig2.update_layout(title="Flood Risk by Area",
                            font=dict(size=14, color='white') ,
                                                                        template="plotly_dark",
                            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig2, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: #a0d2eb;'>Powered by OrbitIQ | PyTorch + Streamlit + Plotly</p>", unsafe_allow_html=True)