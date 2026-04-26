import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")

employees = pd.read_csv("../data/employees.csv")
salaries = pd.read_csv("../data/salaries.csv")
attendance = pd.read_csv("../data/attendance.csv")

attendance.columns = attendance.columns.str.strip()

attendance["employee_id"] = pd.to_numeric(
    attendance["employee_id"],
    errors="coerce"
)

attendance = attendance.dropna(subset=["employee_id"])
attendance["employee_id"] = attendance["employee_id"].astype(int)


attendance["month"] = pd.to_datetime(attendance["month"], errors="coerce")

salary_df = employees.merge(salaries, on="employee_id")
attendance_df = employees.merge(attendance, on="employee_id")

kpi_avg_salary = salary_df["salary"].mean()
kpi_total_bonus = salary_df["bonus"].sum()
kpi_max_salary = salary_df["salary"].max()

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("HR ANALYTICS DASHBOARD", fontsize=18, fontweight="bold")

#Average Salary
avg_salary = (
    salary_df.groupby("department")["salary"]
    .mean()
    .sort_values(ascending=False)
)

avg_salary.plot(kind="bar", ax=axes[0, 0])
axes[0, 0].set_title("Average Salary by Department")
axes[0, 0].set_xlabel("Department")
axes[0, 0].set_ylabel("Salary")
axes[0, 0].tick_params(axis="x", rotation=45)

#Total Bonus
bonus_by_department = (
    salary_df.groupby("department")["bonus"]
    .sum()
    .sort_values(ascending=False)
)

bonus_by_department.plot(kind="bar", ax=axes[0, 1], color="orange")
axes[0, 1].set_title("Total Bonus by Department")
axes[0, 1].set_xlabel("Department")
axes[0, 1].set_ylabel("Bonus")
axes[0, 1].tick_params(axis="x", rotation=45)

#Average Absence
avg_absence = (
    attendance_df.groupby("department")["absence_days"]
    .mean()
    .sort_values(ascending=False)
)

avg_absence.plot(kind="bar", ax=axes[1, 0], color="green")
axes[1, 0].set_title("Average Absence by Department")
axes[1, 0].set_xlabel("Department")
axes[1, 0].set_ylabel("Days")
axes[1, 0].tick_params(axis="x", rotation=45)

#ABSENCE TREND
absence_trend = (
    attendance
    .groupby("month")["absence_days"]
    .mean()
    .sort_index()
)

trend = absence_trend.rolling(window=3, min_periods=1).mean()

axes[1, 1].plot(absence_trend.index, absence_trend.values, label="Avg absence")
axes[1, 1].plot(trend.index, trend.values, label="Trend", linestyle="--", linewidth=2)

axes[1, 1].legend()

axes[1, 1].set_title("Absence Trend Over Time")
axes[1, 1].set_xlabel("Month")
axes[1, 1].set_ylabel("Avg Absence")
axes[1, 1].tick_params(axis='x', rotation=45)
axes[1, 1].legend()

#KPI
axes[0, 2].axis("off")
axes[0, 2].text(0.1, 0.8, f"Avg Salary: {kpi_avg_salary:.2f}", fontsize=14)
axes[0, 2].text(0.1, 0.6, f"Total Bonus: {kpi_total_bonus:.2f}", fontsize=14)
axes[0, 2].text(0.1, 0.4, f"Max Salary: {kpi_max_salary:.2f}", fontsize=14)


axes[1, 2].axis("off")

plt.tight_layout()
plt.savefig("../output/hr_analytics_dashboard_portfolio.png", dpi=300, bbox_inches="tight")
plt.close()