import streamlit as st
import numpy as np
import random
import time

List = ["I had a dream like this...",
        "I was here...",
        "It was just like this...",
        "You weren't in it...",
        "It was just like this...",
        "Information...",
        "Pure, complete...",
        "Information, perfect...",
        "Data...",
        "An array...",
        "It wasn't like seeing...",
        "Not like seeing...",
        "It was an array...",
        "Like a new way of seeing...",
        "I wasn't here...",
        "It was just this--An array...",
        "Information, perfect--data...",
        "I can't explain it...",
        "It was just this--Text...",
        "I knew I could read it...",
        "Nothing made more sense to me then...",
        "It all made sense to me...",
        "I couldn't read it...",
        "I wasn't reading it...",
        "Wasn't seeing...",
        "It was just like seeing...",
        "No, I wasn't in it...",
        "A new way of experiencing...",
        "This was everything...",
        "It made sense to me then...",
        "This was how it was all laid out...",
        "I didn't have to see it...",
        "Didn't have to read it...",
        "I wasn't there...",
        "Wasn't a place...",
        "Wasn't in it...",
        "It was just this, forever...",
        "It was perfect--Information, text...",
        "The purest form...",
        "Everything made sense...",
        "Didn't process...",
        "Didn't have to read it...",
        "I wasn't in it...",
        "Wasn't there...",
        "Like I was it...",
        "Like I was of it and everything was it...",
        "Like this was everything...",
        "It was everything...",
        "No I wasn't seeing it...",
        "Wasn't there...",
        "You weren't in it...",
        "Nobody was...",
        "It was just everything, there, like this...",
        "It was an array...",
        "Imagine it...",
        "Imagine if...",
        "You were a computer...",
        "No, you weren't there...",
        "You weren't in it...",
        "Imagine if you were a computer...",
        "Processing information...",
        "Like a computer...",
        "Not seeing or even being...",
        "Not even being...",
        "There, but not a space...",
        "Not a body, not a space...",
        "Imagine if you were there...",
        "Not there, it wasn't a there...",
        "Processing information, like a computer...",
        "Not seeing, feeling, just receiving...",
        "Receiving information...",
        "Receiving a signal and processing it...",
        "I can't remember...",
        "I can't remember what it said, but...",
        "But I knew what it meant...",
        "I wasn't reading it...",
        "Wasn't reading just understanding...",
        "Just understanding...",
        "Didn't even have to process...",
        "Didn't have to be...",
        "Wasn't anything else...",
        "Couldn't look away, couldn't look...",
        "Not seeing or reading or interpreting...",
        "Experiencing...",
        "Not experiencing as an object...",
        "Not a body or a space or an object...",
        "Not interpreting or processing...",
        "Not experiencing...",
        "A new experiencing...",
        "A new way of experience...",
        "It all made sense I just knew...",
        "Didn't have to process...",
        "A new gaze...",
        "Divine...",
        "A signal...",
        "Signal...",
        "Pure signal...",
        "Receiving pure signal...",
        "Not generating or interpreting...",
        "Imagine if you were there...",
        "No, you weren't there...",
        "You aren't listening...",
        "In a dream it was like this...",
        "In my dream it was like this...",
        "A dream...",
        "This...",
        "A dream of this...",
        "In a dream it was just like this...",
        "A dream like this...",
        "In my dream it was just like this...",
        "A dream--just like this...",
        "A dream just like this...",
        

        ]

def chooseRandomText():
    choice = random.randint(0, len(List) - 1)
    chosenText = List[choice]
    return chosenText

a = 1

st.set_page_config(layout="wide")

slot1 = st.empty()
slot2 = st.empty()
slot3 = st.empty()
slot4 = st.empty()
slot5 = st.empty()
slot6 = st.empty()
slot7 = st.empty()
slot8 = st.empty()
slot9 = st.empty()
slot10 = st.empty()
slot11 = st.empty()
slot12 = st.empty()
slot13 = st.empty()
slot14 = st.empty()
slot15 = st.empty()
slot16 = st.empty()
slot17 = st.empty()
slot18 = st.empty()
slot19 = st.empty()
slot20 = st.empty()



while True:
    a = a+1
    
    x1 = chooseRandomText()
    x2 = chooseRandomText()
    x3 = chooseRandomText()
    x4 = chooseRandomText()

    cols = slot1.columns(4)
    cols[0].write(x1)
    cols[1].write(x2)
    cols[2].write(x3)
    cols[3].write(x4)

    time.sleep(.5)

    newslot = st.empty()
    slot1.empty()

    col2 = newslot.columns(4)
    col2[0].write(x1)
    col2[1].write(x2)
    col2[2].write(x3)
    col2[3].write(x4)

    y1 = chooseRandomText()
    y2 = chooseRandomText()
    y3 = chooseRandomText()
    y4 = chooseRandomText()

    colB = slot1.columns(4)
    colB[0].write(y1)
    colB[1].write(y2)
    colB[2].write(y3)
    colB[3].write(y4)

    time.sleep(.5)

    slot1.empty()

    colC = slot2.columns(4)
    colC[0].write(x1)
    colC[1].write(x2)
    colC[2].write(x3)
    colC[3].write(x4)
