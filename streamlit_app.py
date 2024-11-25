import streamlit as st
import pandas as pd

elements_used = []

# Element dataset as a list of dictionaries
def load_element_data():
    fake_symbols = {"A", "D", "E", "G", "J", "L", "M", "Q", "R", "T", "X", "Z", "Ma", "Di"}
    element_data = [
        {"symbol": "A", "atomic_num": 119, "name": "Awesomium", "atomic_mass": 238},
        {"symbol": "Ac", "atomic_num": 89, "name": "Actinium", "atomic_mass": 227},
        {"symbol": "Ag", "atomic_num": 47, "name": "Silver", "atomic_mass": 107.868},
        {"symbol": "Al", "atomic_num": 13, "name": "Aluminum", "atomic_mass": 26.982},
        {"symbol": "Am", "atomic_num": 95, "name": "Americium", "atomic_mass": 243},
        {"symbol": "Ar", "atomic_num": 18, "name": "Argon", "atomic_mass": 39.948},
        {"symbol": "As", "atomic_num": 33, "name": "Arsenic", "atomic_mass": 74.922},
        {"symbol": "At", "atomic_num": 85, "name": "Astatine", "atomic_mass": 210},
        {"symbol": "Au", "atomic_num": 79, "name": "Gold", "atomic_mass": 196.967},
        {"symbol": "B", "atomic_num": 5, "name": "Boron", "atomic_mass": 10.811},
        {"symbol": "Ba", "atomic_num": 56, "name": "Barium", "atomic_mass": 137.327},
        {"symbol": "Be", "atomic_num": 4, "name": "Beryllium", "atomic_mass": 9.012},
        {"symbol": "Bh", "atomic_num": 107, "name": "Bohrium", "atomic_mass": 264},
        {"symbol": "Bi", "atomic_num": 83, "name": "Bismuth", "atomic_mass": 208.98},
        {"symbol": "Bk", "atomic_num": 97, "name": "Berkelium", "atomic_mass": 247},
        {"symbol": "Br", "atomic_num": 35, "name": "Bromine", "atomic_mass": 79.904},
        {"symbol": "C", "atomic_num": 6, "name": "Carbon", "atomic_mass": 12.011},
        {"symbol": "Ca", "atomic_num": 20, "name": "Calcium", "atomic_mass": 40.078},
        {"symbol": "Cd", "atomic_num": 48, "name": "Cadmium", "atomic_mass": 112.411},
        {"symbol": "Ce", "atomic_num": 58, "name": "Cerium", "atomic_mass": 140.116},
        {"symbol": "Cf", "atomic_num": 98, "name": "Californium", "atomic_mass": 251},
        {"symbol": "Cl", "atomic_num": 17, "name": "Chlorine", "atomic_mass": 35.453},
        {"symbol": "Cm", "atomic_num": 96, "name": "Curium", "atomic_mass": 247},
        {"symbol": "Cn", "atomic_num": 112, "name": "Copernicium", "atomic_mass": 285},
        {"symbol": "Co", "atomic_num": 27, "name": "Cobalt", "atomic_mass": 58.933},
        {"symbol": "Cr", "atomic_num": 24, "name": "Chromium", "atomic_mass": 51.996},
        {"symbol": "Cs", "atomic_num": 55, "name": "Cesium", "atomic_mass": 132.905},
        {"symbol": "Cu", "atomic_num": 29, "name": "Copper", "atomic_mass": 63.546},
        {"symbol": "D", "atomic_num": 120, "name": "Dangerium", "atomic_mass": 240},
        {"symbol": "Db", "atomic_num": 105, "name": "Dubnium", "atomic_mass": 262},
        {"symbol": "Ds", "atomic_num": 110, "name": "Darmstadtium", "atomic_mass": 271},
        {"symbol": "Dy", "atomic_num": 66, "name": "Dysprosium", "atomic_mass": 162.5},
        {"symbol": "E", "atomic_num": 121, "name": "Electrium", "atomic_mass": 242},
        {"symbol": "Er", "atomic_num": 68, "name": "Erbium", "atomic_mass": 167.259},
        {"symbol": "Es", "atomic_num": 99, "name": "Einsteinium", "atomic_mass": 252},
        {"symbol": "Eu", "atomic_num": 63, "name": "Europium", "atomic_mass": 151.964},
        {"symbol": "F", "atomic_num": 9, "name": "Fluorine", "atomic_mass": 18.998},
        {"symbol": "Fe", "atomic_num": 26, "name": "Iron", "atomic_mass": 55.845},
        {"symbol": "Fl", "atomic_num": 114, "name": "Flerovium", "atomic_mass": 289},
        {"symbol": "Fm", "atomic_num": 100, "name": "Fermium", "atomic_mass": 257},
        {"symbol": "Fr", "atomic_num": 87, "name": "Francium", "atomic_mass": 223},
        {"symbol": "G", "atomic_num": 122, "name": "Gloopium", "atomic_mass": 244},
        {"symbol": "Ga", "atomic_num": 31, "name": "Gallium", "atomic_mass": 69.723},
        {"symbol": "Gd", "atomic_num": 64, "name": "Gadolinium", "atomic_mass": 157.25},
        {"symbol": "Ge", "atomic_num": 32, "name": "Germanium", "atomic_mass": 72.64},
        {"symbol": "H", "atomic_num": 1, "name": "Hydrogen", "atomic_mass": 1.007},
        {"symbol": "He", "atomic_num": 2, "name": "Helium", "atomic_mass": 4.002},
        {"symbol": "Hf", "atomic_num": 72, "name": "Hafnium", "atomic_mass": 178.49},
        {"symbol": "Hg", "atomic_num": 80, "name": "Mercury", "atomic_mass": 200.59},
        {"symbol": "Ho", "atomic_num": 67, "name": "Holmium", "atomic_mass": 164.93},
        {"symbol": "Hs", "atomic_num": 108, "name": "Hassium", "atomic_mass": 267},
        {"symbol": "I", "atomic_num": 53, "name": "Iodine", "atomic_mass": 126.904},
        {"symbol": "In", "atomic_num": 49, "name": "Indium", "atomic_mass": 114.818},
        {"symbol": "Ir", "atomic_num": 77, "name": "Iridium", "atomic_mass": 192.217},
        {"symbol": "J", "atomic_num": 123, "name": "Jobium", "atomic_mass": 246},
        {"symbol": "K", "atomic_num": 19, "name": "Potassium", "atomic_mass": 39.098},
        {"symbol": "Kr", "atomic_num": 36, "name": "Krypton", "atomic_mass": 83.798},
        {"symbol": "L", "atomic_num": 124, "name": "Litium", "atomic_mass": 248},
        {"symbol": "La", "atomic_num": 57, "name": "Lanthanum", "atomic_mass": 138.905},
        {"symbol": "Li", "atomic_num": 3, "name": "Lithium", "atomic_mass": 6.941},
        {"symbol": "Lr", "atomic_num": 103, "name": "Lawrencium", "atomic_mass": 262},
        {"symbol": "Lu", "atomic_num": 71, "name": "Lutetium", "atomic_mass": 174.967},
        {"symbol": "Lv", "atomic_num": 116, "name": "Livermorium", "atomic_mass": 292},
        {"symbol": "M", "atomic_num": 125, "name": "Marsium", "atomic_mass": 250},
        {"symbol": "Mc", "atomic_num": 115, "name": "Moscovium", "atomic_mass": 288},
        {"symbol": "Md", "atomic_num": 101, "name": "Mendelevium", "atomic_mass": 258},
        {"symbol": "Mg", "atomic_num": 12, "name": "Magnesium", "atomic_mass": 24.305},
        {"symbol": "Mn", "atomic_num": 25, "name": "Manganese", "atomic_mass": 54.938},
        {"symbol": "Mo", "atomic_num": 42, "name": "Molybdenum", "atomic_mass": 95.96},
        {"symbol": "Mt", "atomic_num": 109, "name": "Meitnerium", "atomic_mass": 268},
        {"symbol": "N", "atomic_num": 7, "name": "Nitrogen", "atomic_mass": 14.007},
        {"symbol": "Na", "atomic_num": 11, "name": "Sodium", "atomic_mass": 22.99},
        {"symbol": "Nb", "atomic_num": 41, "name": "Niobium", "atomic_mass": 92.906},
        {"symbol": "Nd", "atomic_num": 60, "name": "Neodymium", "atomic_mass": 144.242},
        {"symbol": "Ne", "atomic_num": 10, "name": "Neon", "atomic_mass": 20.18},
        {"symbol": "Nh", "atomic_num": 113, "name": "Nihonium", "atomic_mass": 284},
        {"symbol": "Ni", "atomic_num": 28, "name": "Nickel", "atomic_mass": 58.693},
        {"symbol": "No", "atomic_num": 102, "name": "Nobelium", "atomic_mass": 259},
        {"symbol": "Np", "atomic_num": 93, "name": "Neptunium", "atomic_mass": 237},
        {"symbol": "O", "atomic_num": 8, "name": "Oxygen", "atomic_mass": 15.999},
        {"symbol": "Og", "atomic_num": 118, "name": "Oganesson", "atomic_mass": 294},
        {"symbol": "Os", "atomic_num": 76, "name": "Osmium", "atomic_mass": 190.23},
        {"symbol": "P", "atomic_num": 15, "name": "Phosphorus", "atomic_mass": 30.974},
        {"symbol": "Pa", "atomic_num": 91, "name": "Protactinium", "atomic_mass": 231.036},
        {"symbol": "Pb", "atomic_num": 82, "name": "Lead", "atomic_mass": 207.2},
        {"symbol": "Pd", "atomic_num": 46, "name": "Palladium", "atomic_mass": 106.42},
        {"symbol": "Pm", "atomic_num": 61, "name": "Promethium", "atomic_mass": 145},
        {"symbol": "Po", "atomic_num": 84, "name": "Polonium", "atomic_mass": 210},
        {"symbol": "Pr", "atomic_num": 59, "name": "Praseodymium", "atomic_mass": 140.908},
        {"symbol": "Pt", "atomic_num": 78, "name": "Platinum", "atomic_mass": 195.084},
        {"symbol": "Pu", "atomic_num": 94, "name": "Plutonium", "atomic_mass": 244},
        {"symbol": "Q", "atomic_num": 126, "name": "Quebium", "atomic_mass": 252},
        {"symbol": "R", "atomic_num": 127, "name": "Rosalindium", "atomic_mass": 254},
        {"symbol": "Ra", "atomic_num": 88, "name": "Radium", "atomic_mass": 226},
        {"symbol": "Rb", "atomic_num": 37, "name": "Rubidium", "atomic_mass": 85.468},
        {"symbol": "Re", "atomic_num": 75, "name": "Rhenium", "atomic_mass": 186.207},
        {"symbol": "Rf", "atomic_num": 104, "name": "Rutherfordium", "atomic_mass": 261},
        {"symbol": "Rg", "atomic_num": 111, "name": "Roentgenium", "atomic_mass": 272},
        {"symbol": "Rh", "atomic_num": 45, "name": "Rhodium", "atomic_mass": 102.906},
        {"symbol": "Rn", "atomic_num": 86, "name": "Radon", "atomic_mass": 222},
        {"symbol": "Ru", "atomic_num": 44, "name": "Ruthenium", "atomic_mass": 101.07},
        {"symbol": "S", "atomic_num": 16, "name": "Sulfur", "atomic_mass": 32.065},
        {"symbol": "Sb", "atomic_num": 51, "name": "Antimony", "atomic_mass": 121.76},
        {"symbol": "Sc", "atomic_num": 21, "name": "Scandium", "atomic_mass": 44.956},
        {"symbol": "Se", "atomic_num": 34, "name": "Selenium", "atomic_mass": 78.96},
        {"symbol": "Sg", "atomic_num": 106, "name": "Seaborgium", "atomic_mass": 266},
        {"symbol": "Si", "atomic_num": 14, "name": "Silicon", "atomic_mass": 28.086},
        {"symbol": "Sm", "atomic_num": 62, "name": "Samarium", "atomic_mass": 150.36},
        {"symbol": "Sn", "atomic_num": 50, "name": "Tin", "atomic_mass": 118.71},
        {"symbol": "Sr", "atomic_num": 38, "name": "Strontium", "atomic_mass": 87.62},
        {"symbol": "T", "atomic_num": 128, "name": "Teslium", "atomic_mass": 256},
        {"symbol": "Ta", "atomic_num": 73, "name": "Tantalum", "atomic_mass": 180.948},
        {"symbol": "Tb", "atomic_num": 65, "name": "Terbium", "atomic_mass": 158.925},
        {"symbol": "Tc", "atomic_num": 43, "name": "Technetium", "atomic_mass": 98},
        {"symbol": "Te", "atomic_num": 52, "name": "Tellurium", "atomic_mass": 127.6},
        {"symbol": "Th", "atomic_num": 90, "name": "Thorium", "atomic_mass": 232.038},
        {"symbol": "Ti", "atomic_num": 22, "name": "Titanium", "atomic_mass": 47.867},
        {"symbol": "Tl", "atomic_num": 81, "name": "Thallium", "atomic_mass": 204.383},
        {"symbol": "Tm", "atomic_num": 69, "name": "Thulium", "atomic_mass": 168.934},
        {"symbol": "Ts", "atomic_num": 117, "name": "Tennessine", "atomic_mass": 295},
        {"symbol": "U", "atomic_num": 92, "name": "Uranium", "atomic_mass": 238.029},
        {"symbol": "V", "atomic_num": 23, "name": "Vanadium", "atomic_mass": 50.942},
        {"symbol": "W", "atomic_num": 74, "name": "Tungsten", "atomic_mass": 183.84},
        {"symbol": "X", "atomic_num": 129, "name": "Xandium", "atomic_mass": 258},
        {"symbol": "Xe", "atomic_num": 54, "name": "Xenon", "atomic_mass": 131.293},
        {"symbol": "Y", "atomic_num": 39, "name": "Yttrium", "atomic_mass": 88.906},
        {"symbol": "Yb", "atomic_num": 70, "name": "Ytterbium", "atomic_mass": 173.054},
        {"symbol": "Z", "atomic_num": 130, "name": "Zekeium", "atomic_mass": 260},
        {"symbol": "Zn", "atomic_num": 30, "name": "Zinc", "atomic_mass": 65.38},
        {"symbol": "Zr", "atomic_num": 40, "name": "Zirconium", "atomic_mass": 91.224},
        {"symbol": "Ma", "atomic_num": 131, "name": "Marieum", "atomic_mass": 262},
        {"symbol": "Di", "atomic_num": 132, "name": "Divinium", "atomic_mass": 264},
    ]

    # Add status key to each element
    for element in element_data:
        element["status"] = "FAKE😉" if element["symbol"] in fake_symbols else "REAL"
    return element_data

# Function to spell a word using element symbols
def spell_word(word, element_data):
    # Create a dictionary of symbols for quick lookup
    speller_dict = {e["symbol"].lower(): e["symbol"] for e in element_data}

    spelled_out = []
    
    i = 0
    word = word.lower()
    while i < len(word):
        found = False
        # Check for two-character substrings
        for j in range(2, 0, -1):
            if i + j <= len(word):
                substring = word[i:i+j]
                if substring in speller_dict:
                    symbol = speller_dict[substring]
                    spelled_out.append(symbol)
                    elements_used.append(symbol)
                    i += j
                    found = True
                    break
        if not found:
            spelled_out.append(f"<<{word[i]}>>")
            i += 1
    return ' '.join(spelled_out), elements_used

# Streamlit UI
st.title("Periodic Table Word Speller 🧪😃")

# Load the element data
element_data = load_element_data()

# Input field (default value is "Genius")
word = st.text_input(
    "Enter a word or phrase to spell with periodic table elements:", 
    value="Genius"
)

# Button to trigger the spelling process
if st.button("Spell with Elements"):
    spelled_word, elements_used = spell_word(word, element_data)

    # Display the results
    st.write(f"Spelled with elements: **{spelled_word}**")
    st.write(f"Number of element tiles used: **{len(elements_used)}**")
    
    # Updated Copy to Clipboard button with combined result text and element count
    combined_text = f"{spelled_word} --> {len(elements_used)} Tiles needed :)"
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
    
    # Prepare data for display
    element_details = {
    "Atomic Number": [],
    "Symbol": [],
    "Atomic Mass": [],
    "Name": [],
    "Status": []
}
    
    # Collect data for the elements used
    for symbol in elements_used:
        element = next((e for e in element_data if e["symbol"] == symbol), None)
        if element:
            element_details["Atomic Number"].append(element["atomic_num"])
            element_details["Symbol"].append(element["symbol"])
            element_details["Atomic Mass"].append(element["atomic_mass"])
            element_details["Name"].append(element["name"])
            element_details["Status"].append(element["status"])

    # Convert to DataFrame
    df = pd.DataFrame(element_details)

    # Transpose the DataFrame so the headers are in the first column
    #df_transposed = df.T

    # Customize the DataFrame display: thicker and darker lines, hide index
    styled_df = df#_transposed

    # Display the table with headers in the first column and no index
    st.markdown("### Details of Elements Used:")
    st.dataframe(styled_df, hide_index=True)  # Hides the index column

     # Check if any fake elements are used and display a disclaimer
    fake_elements_used = [symbol for symbol in elements_used if 
                          any(e["symbol"] == symbol and e["status"] == "FAKE😉" for e in element_data)]
    if fake_elements_used:
        st.warning(
            "Disclaimer: Your word includes some **fictional elements** (marked as 'FAKE😉'). These are added in so that all spellings can be accomplished and do not exist in the real periodic table!🤓😎"
        )

# Link to Linktree
st.markdown("---")
st.markdown("## Ready to Order?")
st.write("Copy your customized design details and [visit our shop](https://impulse3dprints.etsy.com) to place your order!")
st.markdown("## Find us here!")
st.markdown("🔗 [Visit my Linktree](https://linktr.ee/impulse3d)")
st.markdown("🔗 [Back to our Etsy shop](https://impulse3dprints.etsy.com)")