import streamlit as st
import sympy as sp

st.title("인수분해 계산기")

expr_input = st.text_input("다항식을 입력하세요 (예: x**2 + 2*x + 1):")

if expr_input:
    try:
        # 문자열을 수식으로 변환
        expr = sp.sympify(expr_input)

        # 인수분해 수행
        factors = sp.factor(expr)

        # LaTeX 형식으로 변환
        expr_latex = sp.latex(expr)
        factors_latex = sp.latex(factors)

        # 원래 수식과 인수분해 결과를 LaTeX로 출력
        st.latex(f"{expr_latex} = {factors_latex}")

    except Exception as e:
        st.error(f"오류 발생: {e}")
