import streamlit as st
import pandas as pd


st.header("MLB THE SHOW SHOWDOWN 2025", divider = "blue")
st.subheader("Commissioner: Nick Reiser")

st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATIAAAClCAMAAADoDIG4AAAAz1BMVEX///8EHkK/DT4AADb19/i9ADD99fcAGD4zQl0AFz4AGkC+ADgAHEHNWnK6ACMAADFAS2IaLU0AACy9ADQAAC4AACq7ACoAEzwAADP46u28AC0ACDgAADcAFD27ACcADjrv8PJhanzk5unrwcrKzdOJj5wAACXjqLS4vMN7gpHHO1vy1tynrLVcZXjckJ/Xf5Hms73V19w6R2AmNlOUmqZNWG2tsbrFM1XTcYW5ABftydDckqGCiJbJR2QrOVXQ09htdYXOYnbDJEvw0ti2AACGss1gAAAJqUlEQVR4nO2d60LiOhCAuQgKVCul5WLFgoLKind0XdcL6nn/ZzrgDWgmbZKJzfScfj932UK/bTKZZJLmchkZGRkZGRkZGaRZow7vh5d1IaVrMNzO+0XaHA44P/7oT0kLjcLj2b3g4zUJXL9i5Ylj2T3ODTzWCnqoNZqNM4GHbWwXyet6p7vBuYOTPU3K5pR2juIesRs3HcJmFEecmzgvaXRWaG5GGuvVA9MiJHCOObehq2V+0HiNaJxr9a5pDTJY7j58HxdNrc5qr3xl22l6xmZU6pwb+aX5OeO2zbFt2oEs/il8J50trcoKTU4MWHNMG5DHHcP3ojcCzJzBXzP0TQuQx/Iu4ZvR2zILpb/gt6RkPLZKtQJnTpojQKEGfckgdT3ZO8EN/JhpjgBNKHd6SGG7nGMPQWVac4BZ0DwDvuOqYvrmF1iVVuDPCLrV+N7CgxP084ZOZbVH4CssIl1Zq+i69av+6GE4fJjePAWOvduK/GlWsQc606qsUGC/YG03KSdRtOzi6eR5pUfvDSanvutX+f+Ik6DrjQANNmtaKyYnhofv9Tlp4+Xk2vO5zxonQdcaAUoUlfnusAcLe2d/GNi87tYDTZ/ozAEIKqs4I+7c9BfHVw5HGpyg64wA9JT5dc4wfpXBlQN2anCCXtbYMskpc6ciwuYc19tQn+b3oQ9rjADUlHkTUWMzJh7UOh0wQdcXAYgp8zjzERz2n6Dfegi1bH0RgJYyV+YZe2cEzFNVu1D40BYBSCnzp7LGcrmxx3ZocIKua+KMkjLubHSMM/ZKNvS06ooAlJTxJgljmLjApaAEXVMEIKTM561GxtFnJ6us3R77OU0RgI4yqxg75ueRZwe1YIKuJwLQUVaEJwhFeAa6MyhBL//HlHGLUQSYAsuuUIKuJQKQURaAeY4gPWC1wrKBBF1HBCCjzOZViQkxApYrKtfs53REACrKrF2Msdw+tFgNJeh3+O6MirIWpl3OuIHKbqAEHZ8DUFFWlMvHGY7bwEWhFfQjdASgosxVG/kvfjS4XA2toKMjABVlDs4Yp2VCCTp6JZiIsqpSRr7MGP7VQIKOjQBElLU45WHiXALJ+Rw2QcfmAESUBaop+QIgaZoDrKAjIwARZb70dCxDnbOK3rpiPvobFQGIKMOOMWb0W5xrt5knGJcDEFF2eItWNuGWeLEJOioCkFDWdfHGcrfQYPYDL5yglzE5AAFllr3dwxuLqr1kFxUwEcC8snWp1V4+vFHGHDZBR+QAxpUVxUow4gEnM75gEnREBDCszPLwAzIRZXkn/B+jHgHMKgsC1MTiCr1IZdVqKEFXjwAmlVlOX3lRCVDGGf5/wiToyhHAoLKWrWFoIayMTdBVcwBjyjQNLRZE92V5NkFXjQCmlOkaWkgos/ze6r9QjACGlBXrnD2n6kSNyz4IJ+iKEcCMskB9ZZzLc/zOq3CCrhYBDD1lG3WWLm7AAS6YhAgn6EoRwJCyKgCiKCM3tPMivzq8B11pHcB4wrSgsq2ubBqI7bsKr6CrRABCyjAL5vD6EkCotrS8k2plmIYpvh8ylKAfyTsjpAxTLSWxhTSUoMtHADrKlOs+JZVV8yuJrXwOQEYZ90AVIYT7sjyToEtHADLKginCWG4kc3rMaoIunQOQUcYsaUgxFhjHLlg9JE42AlBR1uKc2CDIPrDHhE+o+FsyAlBR5j2jlOVGToUPo9NeUfb2Z6ck0aERUVZhqwAkmWxz2bAct7icHnRDj/TJwZHElgAiylx9awAQa5fjqe9+hwionOFION2koQwqntbO88hufwzfHCjUCA82aChr8w4G1Mztk1uZT8+Cf/k7Vco8jStN0Qw23CpnCHgnGDhpKHN7PytqmeP8IfxMi7ZMGsryfvcdW1OxQTSjHvjHZw2xCEBEWd56J0CXzKLoCA1qqSj7FOf0khe1REdk/YSWsnxb6wK6PCJrTsSUaajMxiFwEjkxZfjECYnASIOYMitvQNMyL81YZ8SU5XcTG9TCvP29i5typKasbVjZjIuY1QBiyqyWAUdhYiY1aCnrOrjJWU2cRaZOlJQF3s2t+XY54z5yNYCOsq431V5zpshBKpRZ9jYVYSlRZmmvA8WQBmVV3MEiukmBsmqRTqOccxA5yqCgzGrTMpYrv0aNMigoUzwd7yfZjGiaBJQ5hufIQM74WZN5ZSrHfCbAW4GXnhtXVrUM+BDibgueBzKujPPyDAqc/AantU0rQx2O9+NcvALSTCtLctFXhYsC0zoVlM1fWtOKeIGIDP6DAQ1yvIadSStruf7NdHp67Wl5JRimcD0hmLVNSWXrXv+z3LA3tvAN2PganAjhCUc5Zf7T8kB9KFWgCgEWelGj3EQoa4fC28DGOQsXYBLlpaasjH1t53PsTttI7IQq8ZDcN1WVQYf/oV7XarUTuF8dKDdMsAR4A/HKvlR0/nP+ltSUrYPvaztGPGa0pmIjWA0A4so4B9ntqkeAtLTLUA2VuDLOgIB7nl8s2DOek2T57C5hZZYLX4x/nl8cpsvvZFg+WFVcWRW+2K1yDoDbG5cwb1sKyjhTgcrK8AcWJ8qiHshcw8TtWU2e73ogdPd/qtr9azhKNlm+NtOhBxlS222XwR5XnzzST1lF71DWsknURcnwWXoskTA50GD9WjVhqiaxn1Avj9LKoBA3UW6XaRrIflDe0zH5M4g5/zAC/weOMPtZLkoaphiPEdNlSe1a1cdX0oSZyB6pP2Mpmsb44kR+XPZOxTkdfES6/YmvnF3OScW0/zLf09nyi3J2++m0vx24Pm7eX/3VjmbofJfpqayWV1st9rQOSXgpK1k2axhlOkjbsOx+UQtqSllK1uO+eVWZldVLyuYxzkoElKVldemdlaP0TClL1+C/UCCgrEhpN0kcm404ZaghqqiyFE0w3q1WtNeAj+R1VI7FKUvP8tJ5qPLnFfiMzPGZqqQnK38J7ZqovQAfmiTQmaVF2QmzN6d0BHzsMu79DP8XZeWDF7b2f68DfVR5dloca/mk/6ekXazQ+WeLw94Ou1mi9gu8yC2makzU2dJJ/8DbZROkI3Xo/94BfBXe6zl/CqOF2VLKOA9ZLvd8mKwyo3tMpJRtgT3ZnAmuCFYa7Em8GGSU7UHh8pNpAt3ZEomckspBQtneedSFpgmMNJawzSVQ4sq2zqKvNPaU6xMVsMwdKSWqrLHDCZYL9m88mVP0kaBeKoFCTFlj64WdwWC57Lu2H1TWk6ByaKoSqLNVi6FRajbOuaEyzGAy3d5IhCdTA43O42Y0L+dHJ4Z+W0ZGRkZGRkZGRsaP8C9wNSBqHgs+QgAAAABJRU5ErkJggg==")

df = pd.DataFrame(
    {
        "Name": ["Nicky", "Mike", "Logan", "Chase"],
        "Images": [
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&q=80&w=3870",
            "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&q=60&w=600",
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&q=60&w=600",
            "https://images.unsplash.com/photo-1546868871-7041f2a55e12?auto=format&fit=crop&q=60&w=600"
        ],
        "Rank": [1, 2, 3, 4],
        "Win": [0, 1, 2, 1],
        "Loss": [1, 1, 0, 0]
    }
)

st.dataframe(
    df,
    column_config={
        "Images": st.column_config.ImageColumn(),
    },


)

