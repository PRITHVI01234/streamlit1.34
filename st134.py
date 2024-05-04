import streamlit as st
from background import BackgroundCSSGenerator


st.set_page_config(layout="wide", page_title="Streamlit-1.34",page_icon="🚀")

img1_path = r"C:\Users\jofra\Desktop\llama 3\background.jpg"
img2_path = r"C:\Users\jofra\Desktop\ADSAA_Work\Main\Gemini_Generated_Image (2).jpg"
background_generator = BackgroundCSSGenerator(img1_path, img2_path)
page_bg_img = background_generator.generate_background_css()
st.markdown(page_bg_img, unsafe_allow_html=True)

@st.experimental_dialog("🎉 New Streamlit Feature", width="large")
def show_new_streamlit_feature():
    st.markdown("🚀 This is the new Streamlit feature for having a dialog box. Cool, right?")
    
    cool = st.button("Cool!")
    nah_fam = st.button("Nah Fam!")

    if cool:
        st.session_state.response = "cool"
        st.experimental_rerun()
    elif nah_fam:
        st.session_state.response = "nah_fam"
        st.experimental_rerun()

@st.experimental_dialog("Cool 🙌", width="large")
def show_recognition_of_greatness():
    st.markdown("👍 Great choice! Let's explore other amazing features together. Shall we?")
    lets_do_that = st.button("Let's do that")

    if lets_do_that:
        st.session_state.response = "Lets go"
        st.experimental_rerun()


@st.experimental_dialog("Kidding? 😄", width="large")
def show_kidding():
    st.markdown("😂 You're kidding, right? You wouldn't say something like that.")
    yeah_i_was_kidding = st.button("Yeah, I was kidding")
    not_i_am_not = st.button('Not I am Not')

    if yeah_i_was_kidding:
        st.session_state.response = "yeah_i_was_kidding"
        st.experimental_rerun()
    elif not_i_am_not:
        st.session_state.response = "Not_i_am_not"
        st.experimental_rerun()

@st.experimental_dialog("Hmm... 🤔", width="large")
def show_hmm():
    st.markdown("🤨 Hmm... Are you sure you don't think it's cool?👀")
    nana = st.button("Ok I get it its cool!")
    reconsider = st.button("Nah Mate")

    if reconsider:
        st.session_state.response = 'Nah mate'
        st.experimental_rerun()
    elif nana:
        st.session_state.response = 'Ok I get it its cool!'
        st.experimental_rerun()

def show_app_feature():
    st.title("🚀 Explore Streamlit 1.34 Update:")
    st.divider()

    st.write("👀 Welcome to the Streamlit 1.34 documentation! Here, we're excited to showcase the latest enhancements to your Streamlit experience. This document will cover the following features:")
    st.write(":green-background[1. 🗨️ Dialog boxes]")
    st.write(":orange-background[2. 🎨 Colored text backgrounds]")
    st.write(":red-background[3. 🎥 Autoplay/muted videos]")
    st.divider()

    st.header("🌟 **Unveiling Streamlit 1.34 Features:**")
    st.write("Here, we'll demonstrate the prowess of Streamlit's dialogue box feature, text background coloring, and autoplay/muted video capabilities. Explore these features to unlock the full potential of your Streamlit apps.")

    st.header("About ```st.experimental_dialog```:")
    st.write("Key points about st.experimental_dialog:")
    st.write("- Decorate a function with @st.experimental_dialog to create a modal dialog in Streamlit.")
    st.write("- Dialog functions allow for the insertion of modal dialogs into the app.")
    st.write("- Modal dialogs can accept arguments and interact with Session State and other Streamlit elements.")
    st.write("- Users can dismiss modal dialogs by clicking outside, pressing 'ESC', or using the close button. Dismissing a dialog does not trigger an app rerun.")
    st.write("Example:")
    st.markdown("""           
                ```python
                import streamlit as st

                @st.experimental_dialog("Hello Dialog!")
                def my_dialog():
                    st.write("This is a simple dialog box.")
                    if st.button("Close"):
                        st.experimental_rerun()

                # Main app
                if __name__ == "__main__":
                    st.title("Streamlit Experimental Dialog Example")
                    st.write("Click the button below to open the dialog:")

                    if st.button("Open Dialog"):
                        my_dialog()
                ```            
                """)

    st.header(":blue-background[Markdown Background Colors for Text:]")
    st.markdown(
        """
        Elevate your text with vibrant colors! With Streamlit 1.34, you can now set background colors for text in Markdown, bringing visual flair and emphasis to your content.

        Utilize these syntaxes to create text with eye-catching backgrounds:
        
        - :blue-background[blue] 💙
        - :green-background[green] 💚
        - :red-background[red] ❤️
        - :violet-background[violet] 🟣
        - :orange-background[orange] 🟠
        - :gray-background[gray] :grey-background[or grey] 🩶
        - :rainbow-background[rainbow] 🌈

        For instance, transform your text with a blue background:
        
        ```python
        import streamlit as st

        st.write("This is a :blue-background[blue] text with a blue background.")
        ```
        """
    )
    
    st.divider()

    st.header("Autoplay and Mute for st.audio and st.video:")
    st.markdown(
        """
        Dive into seamless multimedia experiences! Streamlit 1.34 introduces the ability to set audio and video elements to autoplay, as well as mute videos to prevent audio playback.

        Check out this example showcasing autoplay and muting a video:
        
        ```python
        import streamlit as st

        st.video("https://www.example.com/video.mp4", autoplay=True, muted=True)
        ```
        """
    )

    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        st.write("")
    with col2:
        st.video("https://youtu.be/lhwclsrszDI", autoplay=True, muted=True)
    with col3:
        st.write("")
    
    st.divider()

    st.subheader("For a comprehensive list of changes, visit the [Official Streamlit Changelog](https://docs.streamlit.io/develop/quick-reference/changelog)")

    st.write("👀 Ready to harness the power of Streamlit? Let's dive in and discover the endless possibilities!")



@st.experimental_dialog("Come on Mate!", width="large")
def show_persuasion():
    st.markdown("Come on, give it a chance! It's really cool, I promise.")
    st.image("download.jpeg")
    okay_fine = st.button("O-Okay... um, okay... It's, um... it's cool.")
    if okay_fine:
        st.session_state.response = 'its cool ig'
        st.experimental_rerun()

def main():   
    if "response" not in st.session_state:
        show_new_streamlit_feature()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    if st.session_state.get("response") == "cool":
        show_recognition_of_greatness()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") == "nah_fam":
        show_kidding()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") == "yeah_i_was_kidding":
        show_recognition_of_greatness()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") == "Maybe it is cool...":
        show_persuasion()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") == 'Not_i_am_not':
        show_hmm()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") ==  'Ok I get it its cool!':
        show_recognition_of_greatness()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") == "Nah mate":
        show_persuasion()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") == 'its cool ig':
        show_recognition_of_greatness()
        st.write("Explore Streamlit's new dialog feature above before moving on! Refresh the page to restart again")
    elif st.session_state.get("response") == 'Lets go':
        show_app_feature()

if __name__ == "__main__":
    main()
