import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

merged_df = pd.read_csv('dashboard/all_data.csv')

st.header("Peminjaman Sepeda")
st.title('Tren Musiman Peminjaman Sepeda')
st.subheader('Total Peminjaman Sepeda Berdasarkan Musim')

season_mapping = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
merged_df['season_day'].map(season_mapping).reset_index()
seasonal_trends = merged_df.groupby(['season_day', 'yr_day'])[['casual_day', 'registered_day']].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x='season_day', y='casual_day', data=merged_df, palette='Set2')
plt.title('Jumlah Peminjaman Casual Berdasarkan Musim')

plt.subplot(1, 2, 2)
sns.boxplot(x='season_day', y='registered_day', data=merged_df, palette='Set3')
plt.title('Jumlah Peminjaman Registered Berdasarkan Musim')

plt.tight_layout()
st.pyplot(plt)

st.subheader('Tren Peminjaman Sepeda per Bulan')

monthly_rentals = merged_df.groupby('mnth_day')[['casual_day', 'registered_day']].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.lineplot(x='mnth_day', y='casual_day', data=monthly_rentals, marker='o', color='skyblue', label='Casual')
sns.lineplot(x='mnth_day', y='registered_day', data=monthly_rentals, marker='o', color='orange', label='Registered')
plt.title('Tren Peminjaman Sepeda oleh Casual dan Registered Berdasarkan Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Peminjaman Sepeda')
plt.xticks(range(1, 13))  
plt.legend()
st.pyplot(plt)

st.title('Dashboard Peminjaman Sepeda')

merged_df['total_rentals'] = merged_df['casual_hour'] + merged_df['registered_hour']
hourly_rentals = merged_df.groupby('hr')['total_rentals'].sum().reset_index()

st.subheader('Jumlah Peminjaman Sepeda per Jam')
plt.figure(figsize=(12, 6))
sns.barplot(x='hr', y='total_rentals', data=hourly_rentals)
plt.title('Jumlah Peminjaman Sepeda per Jam')
plt.xlabel('Jam (0-23)')
plt.ylabel('Total Peminjaman Sepeda')
plt.grid()

st.pyplot(plt)

st.subheader('Distribusi Peminjaman Casual dan Registered')
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
sns.barplot(x='hr', y='casual_hour', data=merged_df, ax=ax[0])
ax[0].set_title('Peminjaman Casual per Jam')
ax[0].set_xlabel('Jam')
ax[0].set_ylabel('Peminjaman Casual')

sns.boxplot(x='hr', y='registered_hour', data=merged_df, ax=ax[1])
ax[1].set_title('Peminjaman Registered per Jam')
ax[1].set_xlabel('Jam')
ax[1].set_ylabel('Peminjaman Registered')

st.pyplot(fig)