import streamlit as st
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def main():
    st.title("Token Image Generator")

    # User inputs
    name = st.text_input("Token Name", "")
    logo = st.file_uploader("Upload Logo Image", type=["jpg", "jpeg", "png"])
    frame = Image.open("frame.png").convert("RGBA")

    if name and logo is not None:
        # Create image
        logo = Image.open(logo).convert("RGBA")
        main_color = logo.getpixel((256, 10))
        back = Image.new(mode="RGBA", size=(1200, 650), color=main_color)

        try:
            # Text
            text_on = f"نمودار و قیمت لحظه‌ای {name}"
            font = ImageFont.truetype("Dana-Black.ttf", size=35, layout_engine=ImageFont.LAYOUT_RAQM)
            I1 = ImageDraw.Draw(frame)
            _, _, w, h = I1.textbbox((0, 0), text_on, font=font)
            I1.text((700 - w, 80), text_on, fill=(255, 255, 255), font=font, align="right", direction="rtl")

            # Logo
            logo = logo.resize((225, 225))
            x, y = logo.size
            back.paste(logo, (329, 320), logo)
            back.paste(frame, (0, 0), frame,)
            st.image(back, use_column_width=True)
        except Exception as e:
            st.error("Error creating image: {}".format(e))

if __name__ == "__main__":
    main()
