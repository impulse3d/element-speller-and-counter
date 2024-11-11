import streamlit as st

# Define periodic table symbols and additional capital letters
periodic_table_symbols = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 
    'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 
    'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 
    'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 
    'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 
    'Lv', 'Ts', 'Og'
]
capitalized_alphabet = ['A', 'D', 'E', 'G', 'J', 'L', 'M', 'Q', 'R', 'T', 'X', 'Z']

# Create a dictionary of symbols with lowercase keys
speller_dict = {s.lower(): s for s in (periodic_table_symbols + capitalized_alphabet)}

# Function to spell a word using element symbols
def spell_word(word):
    spelled_out = []
    elements_used = 0
    i = 0
    word = word.lower()
    while i < len(word):
        found = False
        # Check for two-character substrings
        for j in range(2, 0, -1):
            if i + j <= len(word):
                substring = word[i:i+j]
                if substring in speller_dict:
                    spelled_out.append(speller_dict[substring])
                    i += j
                    elements_used += 1
                    found = True
                    break
        if not found:
            spelled_out.append("<<Not Found>>")
            i += 1
    return ' '.join(spelled_out), elements_used

# Streamlit UI
st.title("Impulse 3d Prints: Periodic Table Speller  🧪😃")

# Callback function to dynamically update output
def update_output():
    spelled_word, element_count = spell_word(st.session_state.word_input)
    st.session_state.spelled_word = spelled_word
    st.session_state.element_count = element_count

# Input field with callback
st.text_input("Enter the word or phrase you want to spell with the periodic table. Then copy the text into your personalization on our etsy page. Be sure to select the right number of tiles for your order!", key="word_input", value="Genius", on_change=update_output)

# Display output dynamically
if "spelled_word" in st.session_state:
    st.write(f"Spelled with elements from Periodic Table: {st.session_state.spelled_word}")
    st.write(f"Number of element tiles used: {st.session_state.element_count}")

# Updated Copy to Clipboard button with combined result text and element count
if st.button("Copy to Clipboard"):
    # Use session state directly for combined text
    combined_text = f" {st.session_state.spelled_word} -- {st.session_state.element_count} Tiles needed :)"
    st.code(combined_text, language="")

    # JavaScript to copy combined text to clipboard
    st.markdown(f"""
    <script>
        const text = `{combined_text}`;
        navigator.clipboard.writeText(text).then(() => {{
            alert("Copied to clipboard!");
        }});
    </script>
    """, unsafe_allow_html=True)

st.markdown("## Ready to Order?")
st.write("Copy your customized design details and [visit our shop](https://impulse3dprints.etsy.com) to place your order!")

# Link to Linktree
st.markdown("---")
st.markdown("## Find us here!")
st.markdown("🔗 [Visit my Linktree](https://linktr.ee/impulse3d)")
st.markdown("🔗 [Back to our etsy shop](https://impulse3dprints.etsy.com)")
