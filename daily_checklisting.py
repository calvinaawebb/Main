
import streamlit as st
import SessionState

session_state = SessionState.get(num_inputs=1, done=False, data={}, area={}, file={})

if st.button("Done"):
   session_state.done = True
clicked = st.button("Add input")

if clicked:
   session_state.num_inputs += 1

#st.markdown(session_state.num_inputs)

if not session_state.done:
   for idx in range(session_state.num_inputs):
       temp = st.text_input("Test", key=idx)
       #st.markdown("Input: {}".format(temp))
       session_state.data[idx] = temp
       #st.markdown("State input: {}".format(session_state.data[idx]))
else:
   for idx, test_value in session_state.data.items():
       #st.markdown("{}: {}".format(idx, test_value))
       print(test_value)
       output = st.checkbox(str(test_value), key=idx)
       session_state.area[idx] = output
for idx, vals in session_state.area.items():
    if vals == True:
        current_thing = session_state.data[idx]
        st.markdown(current_thing)
        fil = st.text_input("Notes", key=idx)
        session_state.file[idx] = fil
        if len(fil) != 0:
            res = current_thing+": "+str(session_state.file[idx])+", "
            f = open("data.txt", "a")
            f.write(res)
            f.close()
