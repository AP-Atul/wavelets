""" Daubechies 13 wavelet """


class Daubechies13:
    """
    Properties
    ----------
    asymmetric, orthogonal, bi-orthogonal

    All values are from http://wavelets.pybytes.com/wavelet/db13/
    """
    __name__ = "Daubechies Wavelet 13"
    __motherWaveletLength__ = 26  # length of the mother wavelet
    __transformWaveletLength__ = 2  # minimum wavelength of input signal

    # decomposition filter
    # low-pass
    decompositionLowFilter = [
        5.2200350984548e-07,
        - 4.700416479360808e-06,
        1.0441930571407941e-05,
        3.067853757932436e-05,
        - 0.0001651289885565057,
        4.9251525126285676e-05,
        0.000932326130867249,
        - 0.0013156739118922766,
        - 0.002761911234656831,
        0.007255589401617119,
        0.003923941448795577,
        - 0.02383142071032781,
        0.002379972254052227,
        0.056139477100276156,
        - 0.026488406475345658,
        - 0.10580761818792761,
        0.07294893365678874,
        0.17947607942935084,
        - 0.12457673075080665,
        - 0.31497290771138414,
        0.086985726179645,
        0.5888895704312119,
        0.6110558511587811,
        0.3119963221604349,
        0.08286124387290195,
        0.009202133538962279
    ]

    # high-pass
    decompositionHighFilter = [
        -0.009202133538962279,
        0.08286124387290195,
        - 0.3119963221604349,
        0.6110558511587811,
        - 0.5888895704312119,
        0.086985726179645,
        0.31497290771138414,
        - 0.12457673075080665,
        - 0.17947607942935084,
        0.07294893365678874,
        0.10580761818792761,
        - 0.026488406475345658,
        - 0.056139477100276156,
        0.002379972254052227,
        0.02383142071032781,
        0.003923941448795577,
        - 0.007255589401617119,
        - 0.002761911234656831,
        0.0013156739118922766,
        0.000932326130867249,
        - 4.9251525126285676e-05,
        - 0.0001651289885565057,
        - 3.067853757932436e-05,
        1.0441930571407941e-05,
        4.700416479360808e-06,
        5.2200350984548e-07
    ]

    # reconstruction filters
    # low pass
    reconstructionLowFilter = [
        0.009202133538962279,
        0.08286124387290195,
        0.3119963221604349,
        0.6110558511587811,
        0.5888895704312119,
        0.086985726179645,
        - 0.31497290771138414,
        - 0.12457673075080665,
        0.17947607942935084,
        0.07294893365678874,
        - 0.10580761818792761,
        - 0.026488406475345658,
        0.056139477100276156,
        0.002379972254052227,
        - 0.02383142071032781,
        0.003923941448795577,
        0.007255589401617119,
        - 0.002761911234656831,
        - 0.0013156739118922766,
        0.000932326130867249,
        4.9251525126285676e-05,
        - 0.0001651289885565057,
        3.067853757932436e-05,
        1.0441930571407941e-05,
        - 4.700416479360808e-06,
        5.2200350984548e-07
    ]

    # high-pass
    reconstructionHighFilter = [
        5.2200350984548e-07,
        4.700416479360808e-06,
        1.0441930571407941e-05,
        - 3.067853757932436e-05,
        - 0.0001651289885565057,
        - 4.9251525126285676e-05,
        0.000932326130867249,
        0.0013156739118922766,
        - 0.002761911234656831,
        - 0.007255589401617119,
        0.003923941448795577,
        0.02383142071032781,
        0.002379972254052227,
        - 0.056139477100276156,
        - 0.026488406475345658,
        0.10580761818792761,
        0.07294893365678874,
        - 0.17947607942935084,
        - 0.12457673075080665,
        0.31497290771138414,
        0.086985726179645,
        - 0.5888895704312119,
        0.6110558511587811,
        - 0.3119963221604349,
        0.08286124387290195,
        - 0.009202133538962279
    ]
