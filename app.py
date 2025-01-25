# Streamlit app code for visualizing Price (Amount) variations with Plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Cleaned Playstore.csv")  # Replace with the actual path if running locally

# Title and description
st.title("Google Play Store Insights")
st.markdown("Explore the variation of different columns in the dataset.")

# Sidebar for column selection
# st.sidebar.title("Navigation")
options = st.sidebar.selectbox("Choose an insight:", [
    "Overview",
    "Most Popular Category",
    
    "Rating Distribution",
    "Top Apps by Reviews",
    "Rating vs Reviews"
    

    
])


# 1. Overview
if options == "Overview":
    st.header("Dataset Overview")
    st.write(f"The dataset contains **{df.shape[0]} rows** and **{df.shape[1]} columns**.")
    st.write(df.head())
    st.write("### Data Summary")
    st.write(df.describe())

# 2. Most Popular Category
elif options == "Most Popular Category":
    st.header("Most Popular Categories by Installs")
    category_installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).reset_index()
    fig = px.bar(category_installs, x="Category", y="Installs", title="Most Popular Categories", labels={"Installs": "Total Installs"})
    st.plotly_chart(fig)



# 3. Rating Distribution
elif options == "Rating Distribution":
    st.header("Average Rating by Category")
    avg_rating_by_category = df.groupby('Category')['Rating'].mean().reset_index()
    fig = px.bar(avg_rating_by_category, x="Category", y="Rating", title="Average Rating by Category",
                  labels={"Category": "App Category", "Rating": "Average Rating"})
    st.plotly_chart(fig)




# 4. Top Apps by Reviews
elif options == "Top Apps by Reviews":
    st.header("Top Apps by Number of Reviews")
    top_reviewed_apps = df.sort_values(by="Reviews", ascending=False).head(10)
    fig = px.bar(top_reviewed_apps, x="App", y="Reviews", title="Apps by Reviews", text="Reviews", 
                 labels={"Reviews": "Number of Reviews"})
    st.plotly_chart(fig)



#5.Rating vs Reviews
elif options == "Rating vs Reviews":
    st.header("Rating vs Reviews for All Apps by Category")
    
    # Create the scatter plot for Rating vs Reviews for all categories
    fig = px.scatter(df, x="Rating", y="Reviews", color="Category", 
                     title="Apps by Rating vs Reviews Across All Categories", 
                     labels={"Rating": "App Rating", "Reviews": "Number of Reviews"},
                     size="Reviews",  # You can adjust the size of the points based on Reviews
                     hover_name="App")  # Show app name on hover
    
    # Display the plot in Streamlit
    st.plotly_chart(fig)

    
    
    




















