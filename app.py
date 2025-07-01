import streamlit as st
import sympy as sp
import re

st.title("🧮 인수분해 계산기")

# 사용자가 입력한 수식을 자동으로 수정하는 함수
def fix_input(expr):
    expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)  # 2x → 2*x
    expr = expr.replace("^", "**")                    # x^2 → x**2
    return expr

# 수식 입력
expr_input = st.text_input("다항식을 입력하세요 (예: x^2 + 2x + 1):")

if expr_input:
    try:
        # 입력값 자동 수정
        fixed_expr = fix_input(expr_input)
        
        # 수식을 sympy로 변환
        expr = sp.sympify(fixed_expr)

        # 인수분해
        factors = sp.factor(expr)

        # 결과 출력
        st.markdown(f"### 📌 해석된 수식:\n`{expr}`")
        st.markdown(f"### ✅ 인수분해 결과:\n`{factors}`")
    
    except Exception as e:
        st.error(f"오류 발생: {e}")
