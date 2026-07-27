import streamlit as st
import math

# ================= 核心数据（与桌面版一致） =================
valve_data = {
    (15, 150): (0.012, 8), (15, 300): (0.012, 8), (15, 600): (0.012, 8),
    (15, 900): (0.012, 8), (15, 1500): (0.012, 8), (15, 2500): (0.012, 8),
    (20, 150): (0.018, 10), (20, 300): (0.018, 10), (20, 600): (0.018, 10),
    (20, 900): (0.018, 10), (20, 1500): (0.018, 10), (20, 2500): (0.018, 10),
    (25, 150): (0.022, 18), (25, 300): (0.022, 18), (25, 600): (0.022, 18),
    (25, 900): (0.022, 18), (25, 1500): (0.020, 18), (25, 2500): (0.022, 18),
    (40, 150): (0.035, 25), (40, 300): (0.035, 25), (40, 600): (0.035, 25),
    (40, 900): (0.035, 25), (40, 1500): (0.035, 25), (40, 2500): (0.035, 25),
    (50, 150): (0.040, 43), (50, 300): (0.040, 43), (50, 600): (0.040, 43),
    (50, 900): (0.040, 43), (50, 1500): (0.040, 43), (50, 2500): (0.040, 43),
    (65, 150): (0.058, 45), (65, 300): (0.058, 45), (65, 600): (0.058, 45),
    (65, 900): (0.058, 45), (65, 1500): (0.058, 45), (65, 2500): (0.058, 45),
    (80, 150): (0.065, 160), (80, 300): (0.065, 160), (80, 600): (0.065, 160),
    (80, 900): (0.065, 160), (80, 1500): (0.065, 160), (80, 2500): (0.065, 160),
    (100, 150): (0.084, 210), (100, 300): (0.084, 210), (100, 600): (0.084, 210),
    (100, 900): (0.084, 210), (100, 1500): (0.084, 210), (100, 2500): (0.084, 210),
    (150, 150): (0.126, 550), (150, 300): (0.126, 550), (150, 600): (0.126, 550),
    (150, 900): (0.126, 550), (150, 1500): (0.126, 550), (150, 2500): (0.126, 550),
    (200, 150): (0.148, 935), (200, 300): (0.148, 935), (200, 600): (0.148, 935),
    (200, 900): (0.148, 935), (200, 1500): (0.148, 935), (200, 2500): (0.148, 935),
    (250, 150): (0.200, 1622), (250, 300): (0.200, 1622), (250, 600): (0.200, 1622),
    (250, 900): (0.200, 1622), (250, 1500): (0.105, 1622), (250, 2500): (0.200, 1622),
    (300, 150): (0.250, 2550), (300, 300): (0.250, 2550), (300, 600): (0.250, 2550),
    (300, 900): (0.250, 2550), (300, 1500): (0.225, 2550), (300, 2500): (None, None),
    (350, 150): (0.268, 2832), (350, 300): (0.268, 2832), (350, 600): (0.268, 2832),
    (350, 900): (0.268, 2832), (350, 1500): (0.240, 2832), (350, 2500): (None, None),
    (400, 150): (0.305, 3380), (400, 300): (0.305, 3380), (400, 600): (0.325, 3380),
    (400, 900): (0.285, 3380), (400, 1500): (0.298, 3380), (400, 2500): (None, None),
    (450, 150): (0.340, 5633), (450, 300): (0.340, 5633), (450, 600): (0.340, 5633),
    (450, 900): (0.340, 5633), (450, 1500): (0.340, 5633), (450, 2500): (None, None),
    (500, 150): (0.390, 6252), (500, 300): (0.390, 6252), (500, 600): (0.390, 6252),
    (500, 900): (0.370, 6252), (500, 1500): (0.380, 6252), (500, 2500): (None, None),
    (600, 150): (0.482, 8273), (600, 300): (0.482, 8273), (600, 600): (0.450, 7384),
    (600, 900): (0.450, 7384), (600, 1500): (0.450, 7384), (600, 2500): (None, None),
    (700, 150): (0.495, 13624), (700, 300): (0.495, 13624), (700, 600): (0.495, 13624),
    (700, 900): (0.508, 13996), (700, 1500): (0.495, 13624), (700, 2500): (None, None),
    (750, 150): (0.522, 13696), (750, 300): (0.522, 13696), (750, 600): (0.522, 13696),
    (750, 900): (None, None), (750, 1500): (None, None), (750, 2500): (None, None),
    (800, 150): (0.684, 18943), (800, 300): (0.677, 18327), (800, 600): (0.650, 17653),
    (800, 900): (0.650, 17653), (800, 1500): (None, None), (800, 2500): (None, None),
    (900, 150): (0.714, 26165), (900, 300): (0.714, 26165), (900, 600): (0.714, 26165),
    (900, 900): (None, None), (900, 1500): (None, None), (900, 2500): (None, None),
    (1000, 150): (0.777, 29669), (1000, 300): (0.777, 29669), (1000, 600): (0.703, 25230),
    (1000, 900): (0.703, 25230), (1000, 1500): (None, None), (1000, 2500): (None, None),
    (1050, 150): (0.850, 36724), (1050, 300): (None, None), (1050, 600): (None, None),
    (1050, 900): (None, None), (1050, 1500): (None, None), (1050, 2500): (None, None),
    (1100, 150): (0.850, 36724), (1100, 300): (0.850, 36724), (1100, 600): (None, None),
    (1100, 900): (None, None), (1100, 1500): (None, None), (1100, 2500): (None, None),
    (1200, 150): (0.850, 36724), (1200, 300): (0.850, 36724), (1200, 600): (0.850, 36724),
    (1200, 900): (0.850, 36724), (1200, 1500): (None, None), (1200, 2500): (None, None),
    (1300, 150): (0.850, 36093), (1300, 300): (0.940, 40908), (1300, 600): (0.940, 40908),
    (1300, 900): (None, None), (1300, 1500): (None, None), (1300, 2500): (None, None),
    (1350, 150): (0.940, 40908), (1350, 300): (0.940, 60062), (1350, 600): (None, None),
    (1350, 900): (None, None), (1350, 1500): (None, None), (1350, 2500): (None, None),
    (1400, 150): (0.940, 40905), (1400, 300): (1.150, 60062), (1400, 600): (None, None),
    (1400, 900): (None, None), (1400, 1500): (None, None), (1400, 2500): (None, None),
    (1500, 150): (1.080, 52317), (1500, 300): (None, None), (1500, 600): (None, None),
    (1500, 900): (None, None), (1500, 1500): (None, None), (1500, 2500): (None, None),
    (1600, 150): (0.940, 40905), (1600, 300): (1.416, 86111), (1600, 600): (None, None),
    (1600, 900): (None, None), (1600, 1500): (None, None), (1600, 2500): (None, None),
    (1800, 150): (1.310, 67625), (1800, 300): (1.310, 67625), (1800, 600): (None, None),
    (1800, 900): (None, None), (1800, 1500): (None, None), (1800, 2500): (None, None),
    (2000, 150): (1.628, 110683), (2000, 300): (None, None), (2000, 600): (None, None),
    (2000, 900): (None, None), (2000, 1500): (None, None), (2000, 2500): (None, None),
}

dn_list = sorted(set(k[0] for k in valve_data.keys()))
class_list = [150, 300, 600, 900, 1500, 2500]


# ================= 辅助计算函数（复制自原逻辑） =================
def calc_density(medium, dens_input, densN, P, T, M):
    if dens_input is not None and dens_input > 0:
        return dens_input
    P_abs_MPa = P + 0.101325
    if densN is not None and densN > 0:
        return 273.15 * densN * P_abs_MPa / 0.1 / (273.15 + T)
    P_abs_Pa = (P + 0.101325) * 1e6
    rho_air = P_abs_Pa / (287.058 * (T + 273.15))
    return rho_air if medium == "空气" else rho_air * M / 29.0


# ================= 页面布局 =================
st.set_page_config(page_title="轴流式止回阀计算器", layout="wide")
st.title("🔧 轴流式止回阀综合计算工具")

# 创建两个选项卡（完美对应原桌面版的两个 Tab）
tab1, tab2 = st.tabs(["止回阀选型计算", "弹簧设计计算"])

# ================= Tab 1：止回阀选型计算 =================
with tab1:
    col_inputs, col_results = st.columns([1, 1])

    with col_inputs:
        st.subheader("📥 输入参数")
        st.write("---")

        dn_val = st.selectbox("公称通径 DN", options=dn_list, index=0)
        class_val = st.selectbox("压力等级 Class", options=class_list, index=0)

        # 根据 DN 和 Class 动态提取结构参数（手机端也能实时联动）
        key = (dn_val, class_val)
        d_curr, cv_curr = valve_data.get(key, (None, None))
        if d_curr and cv_curr:
            st.caption(f"🏷️ 当前规格：喉径 d = **{d_curr} m**, 额定 Cv = **{cv_curr}**")
        else:
            st.error("所选规格数据缺失，请更换 DN 或 Class")

        medium = st.selectbox("介质", options=["空气", "其他"], index=0)
        mol = st.number_input("分子量 M (空气=29)", value=29.0, step=1.0)

        st.write("---")
        col_f1, col_f2, col_f3 = st.columns(3)
        with col_f1:
            qv_val = st.number_input("Qv (m³/h)", value=100.0, step=10.0)
        with col_f2:
            qn_val = st.number_input("Qn (Nm³/h)", value=0.0, step=10.0)
        with col_f3:
            qm_val = st.number_input("Qm (kg/h)", value=0.0, step=10.0)

        temp = st.number_input("温度 T (℃)", value=20.0, step=5.0)
        press = st.number_input("压力 P (MPaG)", value=0.1, step=0.05)
        dens_input = st.number_input("密度 ρ (kg/m³) 选填", value=0.0, step=1.0)
        densN_input = st.number_input("标况密度 ρN (选填)", value=0.0, step=0.1)

        st.write("---")
        st.caption("⚙️ 力学参数")
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            fn_val = st.number_input("全开载荷 FN (N)", value=100.0, step=10.0)
        with col_m2:
            g_val = st.number_input("阀芯重力 G (N)", value=50.0, step=10.0)
        with col_m3:
            mu_val = st.number_input("摩擦系数 μ", value=0.2, step=0.05)

    with col_results:
        st.subheader("✅ 计算结果")
        st.write("---")
        if qv_val <= 0 and qn_val <= 0 and qm_val <= 0:
            st.warning("请至少输入一个大于 0 的流量值")
        elif not d_curr or not cv_curr:
            st.error("无法计算，该规格数据缺失")
        else:
            try:
                # 统一换算成 Qv
                qv = None
                if qv_val > 0:
                    qv = qv_val
                elif qn_val > 0:
                    P_abs_kPa = press * 1000 + 101.325
                    qv = qn_val * 101.325 * (temp + 273.15) / 273.15 / P_abs_kPa
                elif qm_val > 0:
                    rho_calc = calc_density(medium, dens_input if dens_input > 0 else None,
                                            densN_input if densN_input > 0 else None, press, temp, mol)
                    qv = qm_val / rho_calc

                # 密度计算
                rho = calc_density(medium, dens_input if dens_input > 0 else None,
                                   densN_input if densN_input > 0 else None, press, temp, mol)

                # 开度计算
                A_min = 0.785 * d_curr ** 2
                V1 = qv / (3600 * A_min)
                V2 = math.sqrt((fn_val + mu_val * g_val) / (rho * A_min))
                K = V1 / V2

                if K >= 1.0:
                    cv_actual = cv_curr
                    k_disp = "100% (全开)"
                else:
                    cv_actual = cv_curr * K
                    k_disp = f"{K * 100:.2f}%"

                # 压降计算
                Sg = rho / 1000.0
                Qv_gal = (qv * 1000) / (60 * 3.7854)
                delta_P = Sg * 1e6 / ((cv_actual / Qv_gal) ** 2 * 145) if cv_actual > 0 else float('inf')

                # 输出结果 (使用 metric 组件，适合手机端瀑布流展示)
                col1, col2 = st.columns(2)
                col1.metric(label="工况体积流量 Qv", value=f"{qv:.2f} m³/h")
                col2.metric(label="工况密度 ρ", value=f"{rho:.3f} kg/m³")

                col3, col4 = st.columns(2)
                col3.metric(label="喉部流速 V1", value=f"{V1:.2f} m/s")
                col4.metric(label="全开速度 V2", value=f"{V2:.2f} m/s")

                col5, col6 = st.columns(2)
                col5.metric(label="阀门开度 K", value=k_disp)
                col6.metric(label="有效流量系数 Cv", value=f"{cv_actual:.2f}")

                st.write("---")
                st.metric(label="🔥 阀门压降 ΔP", value=f"{delta_P:.2f} Pa", delta_color="inverse")

            except Exception as e:
                st.error(f"计算发生异常：{e}")

# ================= Tab 2：弹簧设计计算 =================
with tab2:
    col_spring_in, col_spring_out = st.columns([1, 1])

    with col_spring_in:
        st.subheader("📥 弹簧输入参数")
        st.write("---")

        sW = st.number_input("阀芯组件自重 W (Kg)", value=14.25, step=0.1)
        sF1 = st.number_input("阀关时弹簧压缩量 F1 (mm)", value=96.0, step=1.0)
        sho = st.number_input("阀门升程 ho (mm)", value=76.0, step=1.0)
        sG = st.number_input("弹簧剪切弹性模量 G (MPa)", value=70000.0, step=1000.0)
        sd = st.number_input("弹簧丝直径 d (mm)", value=4.0, step=0.5)
        sD2 = st.number_input("弹簧中径 D2 (mm)", value=80.0, step=1.0)
        sN = st.number_input("实取弹簧有效圈数 N", value=7.0, step=1.0)
        sHn = st.number_input("实取弹簧工作高度 Hn (mm)", value=103.0, step=1.0)
        stau = st.number_input("弹簧许用剪切应力 τ (MPa)", value=630.0, step=10.0)

    with col_spring_out:
        st.subheader("✅ 弹簧计算结果")
        st.write("---")

        if sF1 <= 0 or sD2 <= 0 or sN <= 0 or sd <= 0:
            st.warning("弹簧直径、圈数、压缩量参数需大于 0")
        else:
            try:
                R1 = 0.4 * 9.8 * sW
                Fdmin = R1 / sF1
                Fn = sF1 + sho
                Fd = (sG * sd ** 4) / (8 * sD2 ** 3 * sN)

                P1 = Fd * sF1
                Pn = Fd * Fn

                C = sD2 / sd
                K = (4 * C - 1) / (4 * C - 4) + 0.615 / C
                Pnj = (math.pi * sd ** 3) / (8 * K * sD2) * stau

                Ho = sHn + Fn
                t = (Ho - 1.5 * sd) / sN
                alpha = math.atan(t / (math.pi * sD2))
                D_max = 0.8 * (sD2 - sd)
                D_min = 1.2 * (sD2 + sd)
                L = math.pi * sD2 * (sN + 2)
                lam = Ho / sD2

                # 使用指标块显示
                st.caption("📊 弹簧力与刚度")
                col1, col2, col3 = st.columns(3)
                col1.metric("阀关力 R1", f"{R1:.2f} N")
                col2.metric("最小刚度 Fdmin", f"{Fdmin:.3f} N/mm")
                col3.metric("计算刚度 Fd", f"{Fd:.3f} N/mm")

                st.caption("⚙️ 载荷特性")
                col4, col5, col6 = st.columns(3)
                col4.metric("关闭力 P1", f"{P1:.1f} N")
                col5.metric("全开力 Pn", f"{Pn:.1f} N")
                col6.metric("极限载荷 Pnj", f"{Pnj:.0f} N")

                st.caption("📐 几何特性")
                col7, col8 = st.columns(2)
                col7.metric("自由高度 Ho", f"{Ho:.1f} mm")
                col8.metric("节距 t", f"{t:.2f} mm")

                st.write("---")
                st.subheader("✅ 判定结果")
                col_j1, col_j2 = st.columns(2)
                col_j1.success("✔ 弹簧屈度系数 (C > 4) 合格" if C > 4 else "❌ 不合格")
                col_j2.success("✔ 弹簧稳定性 (λ < 5.3) 合格" if lam < 5.3 else "❌ 不稳定")

            except Exception as e:
                st.error(f"计算发生异常：{e}")
