import streamlit as st
import matplotlib.pyplot as plt
st.title('Hardy-Weinberg Equilibrium')


CH = st.sidebar.number_input('Common Homozygotes', value=1.)
H = st.sidebar.number_input('Heterozygotes', value=1.)
RH= st.sidebar.number_input('Rare Homozygotes', value=1.)
ECH = st.sidebar.number_input('Expected Common Homozygotes', value=1.)
EH = st.sidebar.number_input('Expected  Heterozygotes', value=1.)
ERH = st.sidebar.number_input('Expected Rare Homozygotes', value=1.)

pfreq = st.sidebar.number_input('p Allele Frequency', 
        value=1.,
        min_value=0., 
        max_value=100.,
        step=0.05,
        )

qfreq = st.sidebar.number_input('q Allele Frequency', 
        value=1.,
        min_value=0., 
        max_value=100.,
        step=0.05,
        )

chi1 = ((CH-ECH) * (CH-ECH)) / ECH
chi2 = ((H-EH) * (H-EH)) / EH
chi3 = ((RH-ERH) * (RH-ERH)) / ERH
chisqr = (chi1 + chi2 + chi3)
st.write(chi1, chi2, chi3, chisqr)

fig, ax = plt.subplots()
ax.plot(chi1, label='ch1')
ax.plot(chi2, label='ch2')
ax.plot(chi3, label='ch3')
ax.legend()

st.write(fig)
