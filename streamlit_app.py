import streamlit as st
from streamlit_echarts import st_echarts
import yaml
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

# Function to check if YAML is valid
def is_valid_yaml(yaml_str):
    try:
        yaml.load(yaml_str, Loader=yaml.Loader)
        return True
    except Exception as e:
        return False



# # Function for the YAML editor page
def yaml_editor_page():
    st.title("Policy Editor and Validator")

    # Input text area for YAML editing
    yaml_input = st.text_area("Enter Policy Details Here. The Editor validate the policy by using cloud custodian", height=350)
    validate_button_disabled = not yaml_input.strip()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("VALIDATE POLICY", disabled=validate_button_disabled):
            if is_valid_yaml(yaml_input):
                st.success("Policy is valid ..!")
                st.balloons()
            else:
                st.error("Policy is not valid. Please check the syntax..!")
    with col2:
        st.button("SUBMIT")
        
    with col3:
        st.button("CANCEL")
 

    # Display parsed YAML
    st.subheader("Parsed Policy :")
    try:
        yaml_data = yaml.load(yaml_input, Loader=yaml.Loader)
        st.write(yaml_data)
    except Exception as e:
        st.error(f"Error parsing Policy: {str(e)}")
        


def taggig():
    st.title("Tagging")

    # Create a sample dataframe
    df = pd.DataFrame({
        'Subscriptions': ['sub-crop-nas-non-prod-1', 'sub-crop-nas-prod-3', 'sub-crop-qa-ut-6', 'sub-crop-qa-prod-1', 'sub-uat-nas-non-prod3'],
        'Us-East-1': [23,45,65,34,31],
        'Us-East-2': [12,45,67,88,90],
        'Global': [23,45,67,89,78],
        'Us-West-1': [80,56,7,88,23],
        'Us-West-2': [12,45,77,80,90],
        'Grand Total': [111, 243, 365, 784, 985],
    })

    # selected_indices = st.multiselect('Select rows:', df.index)
    

    # selected_columns = st.multiselect('Select columns:', df.columns)
    # df_selected_columns = df[selected_columns]
    # st.dataframe(df_selected_columns, hide_index=True)


    st.write('The subscriptions of resources across all the regions:')
    st.dataframe(df,hide_index=True)

    # pd.DataFrame(data)
    # st.dataframe(data,hide_index=True)

    col1, col2 = st.columns(2)

    with col1:
        # Add a multiselect widget to select rows based on the index
        selected_indices = st.multiselect('Select :', df.index)
        # Subset the dataframe with the selected indices
        selected_rows = df.loc[selected_indices]

        # Display the selected data
        # st.write('Selected Rows:')
        st.dataframe(selected_rows,hide_index=True)

    with col2:
        selected_columns = st.multiselect('Select :', df.columns)
        df_selected_columns = df[selected_columns]
        st.dataframe(df_selected_columns, hide_index=True)
    # st.write('Dataframe:')
    # st.dataframe(df,hide_index=True)



def resources():
    st.title("Resources")
    st.subheader("The List of All Resources")
    st.write("The resources untagged and or tagged can be get filterd out based on any criteria and selection "
             "from the list of dynamic filter table and data available")

    data = {
        'Cloud': ['Azure', 'AWS ', 'GCP', 'Oracle', 'IBM', 'Alibaba', 'Onprime'],
        'PDF Number': [12322,23242,12343,2343,2341,6543,6543],
        'Customer Name': ['Mr.Bean Shah', 'Mr.Bean Shah', 'Prasad J', 'Rahul K', 'Kumar Sanu', 'Shahank Raj', 'Mr.Bean Shah'],
        'Agency Address': ['Mr.Bean Shah', 'Mr.Bean Shah', 'Prasad J', 'Rahul K', 'Kumar Sanu', 'Shahank Raj', 'Mr.Bean Shah'],
        'Phone Number': [12322,23242,12343,2343,2341,6543,6543],
        'FAX Number': [12322,23242,12343,2343,2341,6543,6543],
        'Email Address': ['prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com'],
        'Praposed Date': [12322,23242,12343,2343,2341,6543,6543],
        'Expected Date': [12322,23242,12343,2343,2341,6543,6543],
        'Applicant Name': ['Mr.Bean Shah', 'Mr.Bean Shah', 'Prasad J', 'Rahul K', 'Kumar Sanu', 'Shahank Raj', 'Mr.Bean Shah'],
        'Applicant Email': ['prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com', 'prasad@gmail.com'],
        'Applicant GL Code': [12322,23242,12343,2343,2341,6543,6543],
        'Applicant SIC': [12322,23242,12343,2343,2341,6543,6543],
        'Applicant NAICS': [12322,23242,12343,2343,2341,6543,6543],
        'Applicant FEIN': [12322,23242,12343,2343,2341,6543,6543],
        }

    df = pd.DataFrame(data)

    dynamic_filters = DynamicFilters(df, filters=['Cloud', 'PDF Number', 'Customer Name'])

    with st.sidebar:
        dynamic_filters.display_filters()

    dynamic_filters.display_df(hide_index=True)   
    submit_button = st.button("SUBMIT")

    if submit_button:
        dynamic_filters.display_df(hide_index=True)
        st.success("Submitted Successfully..!")
        st.balloons()



def template():
    st.title("Policy Templates")
    
    # col_names = ["Resource Group Policy", "Tagging Policy", "Resource Group Policy","Tagging Policy"]
    # image_url = "https://avatars.githubPrasadcontent.com/u/103177420?v=4"

    # for _ in range(2):  # Repeat for 3 rows
    #     cols = st.columns(2)
    #     for i, col in enumerate(cols):
    #         with col:
    #             st.caption(col_names[i])
    #             st.image(image_url)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Resource Group Policy")
        st.image("https://avatars.githubusercontent.com/u/103177428?v=4")

    with col2:
        st.write("Tagging Policy")
        st.image("https://avatars.githubusercontent.com/u/103177422?v=4")

    with col3:
        st.write("Policy")
        st.image("https://avatars.githubusercontent.com/u/103177423?v=4")


def help():
    st.title("Help Page")

    st.image("geico.png")

    st.subheader("This is GEICO specific mulicloud resource tagging management and policy compliance dashbord developed for poc and reaserch and developement "
                 "perspective. Feel free to reach out to prasad.jivane@valuemomentum.com for any clarifications or information required..!")


# Function for the main app page
def main_page():

    col1, col2 = st.columns(2)

    with col1:
        st.title("GEICO Multi Cloud Dashboard")
        st.write('Compliance per Line of Business')
            # st.write("Cloud Complaince")

            # Sample data
        data = {
                'Business': ['Sales', 'Services', 'Policy', 'Underwritig'],
                'Line of Business': ['Product', 'Services', 'Technology', 'Research'],
                'Cost Center': ['LOB1', 'LOB2', 'LOB3', 'LOB4'],
                'Billing': ['C001', 'C002', 'C003', 'C004'],
                'Business Owner': ['Mr.Bean','Mr.Bean','Mr.Bean','Mr.Bean'],
                'Technnical Owner': ['Prasad', 'Prasad','Prasad','Prasad'],
                'Environment': ['Devlopment', 'Testing', 'Staging','Production'],
                'Budget': ['$2282','$5560','$9032','$9438'],
                'Creation Date': ['10-02-2022','25-12-2018','26-11-2020','11-09-2012'],
            }

            # Create a DataFrame
        pd.DataFrame(data)
        st.dataframe(data,hide_index=True)

            # Display the table
            # st.table(df)

    with col2:
        options = {
            "title": {"text": "Cloud Compliance", "subtext": "GEICO", "left": "center"},
            "tooltip": {"trigger": "item"},
            "legend": {"orient": "vertical", "right": "right"},
            "series": [
                {
                    "name": "Compliance %",
                    "type": "pie",
                    "radius": "60%",
                    "data": [
                        {"value": 20, "name": "AWS"},
                        {"value": 20, "name": "GCP"},
                        {"value": 15, "name": "IBM"},
                        {"value": 15, "name": "ORACLE"},
                        {"value": 30, "name": "AZURE"},
                    ],
                    "emphasis": {
                        "itemStyle": {
                            "shadowBlur": 10,
                            "shadowOffsetX": 0,
                            "shadowColor": "rgba(0, 0, 0, 0.5)",
                        }
                    },
                }
            ],
        }
        st_echarts(
            options=options, height="450px",
        )



    # st.title("GEICO Multi Cloud Dashboard")
    # st.write('Compliance per Line of Business')
    # # st.write("Cloud Complaince")

    # # Sample data
    # data = {
    #     'Company': ['ValueMomentum', 'GEICO', 'Broadridge', 'Wipro'],
    #     'Line of Business': ['Product', 'Services', 'Technology', 'Research'],
    #     'Cost Center': ['LOB1', 'LOB2', 'LOB3', 'LOB4'],
    #     'App Name': ['Analytics', 'Business', 'Maagement', 'Automation'],
    #     'Business Owner': ['Mr.Bean','Mr.Bean','Mr.Bean','Mr.Bean'],
    #     'Technnical Owner': ['Prasad', 'Prasad','Prasad','Prasad'],
    #     'Environment': ['Devlopment', 'Testing', 'Staging','Production'],
    #     'Budget': ['$2282','$5560','$9032','$9438'],
    #     'Creation Date': ['10-02-2022','25-12-2018','26-11-2020','11-09-2012'],
    # }

    # # Create a DataFrame
    # pd.DataFrame(data)
    # st.dataframe(data,hide_index=True)

    # # Display the table
    # # st.table(df)

    # options = {
    #     "title": {"text": "Cloud Compliance", "subtext": "GEICO", "right": "center"},
    #     "tooltip": {"trigger": "item"},
    #     "legend": {"orient": "vertical", "left": "left",},
    #     "series": [
    #         {
    #             "name": "Usage",
    #             "type": "pie",
    #             "radius": "60%",
    #             "data": [
    #                 {"value": 1048, "name": "AWS"},
    #                 {"value": 735, "name": "GCP"},
    #                 {"value": 580, "name": "AZURE"},
    #                 {"value": 484, "name": "ORACLE"},
    #                 {"value": 300, "name": "IBM"},
    #             ],
    #             "emphasis": {
    #                 "itemStyle": {
    #                     "shadowBlur": 10,
    #                     "shadowOffsetX": 0,
    #                     "shadowColor": "rgba(0, 0, 0, 0.5)",
    #                 }
    #             },
    #         }
    #     ],
    # }
    # st_echarts(
    #     options=options, height="450px",
    # )


    options = {
    "title": {"text": "Compliance Timeline", "subtext": "# Non Compliance Events"},
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {"type": "cross", "label": {"backgroundColor": "#6a7985"}},
    },
    "legend": {"data": ["Low", "Medium", "Avg", "Critical", "High"]},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "grid": {"left": "1%", "right": "2%", "Bpttom":"3%","containLabel": True},
    "xAxis": [
        {
            "type": "category",
            "boundaryGap": False,
            "data": ["Jan", "Feb", "March", "April", "May", "June", "July"],
        }
    ],
    "yAxis": [{"type": "value"}],
    "series": [
        {
            "name": "Low",
            "type": "line",
            "areaStyle": {},
            "emphasis": {"focus": "series"},
            "data": [120, 132, 101, 134, 90, 230, 210],
        },
        {
            "name": "Medium",
            "type": "line",
            "stack": "总量",
            "areaStyle": {},
            "emphasis": {"focus": "series"},
            "data": [220, 182, 191, 234, 290, 330, 310],
        },
        {
            "name": "Avg",
            "type": "line",
            "stack": "总量",
            "areaStyle": {},
            "emphasis": {"focus": "series"},
            "data": [150, 232, 201, 154, 190, 330, 410],
        },
        {
            "name": "Critical",
            "type": "line",
            "stack": "总量",
            "areaStyle": {},
            "emphasis": {"focus": "series"},
            "data": [320, 332, 301, 334, 390, 330, 320],
        },
        {
            "name": "High",
            "type": "line",
            "stack": "总量",
            "label": {"show": True, "position": "top"},
            "areaStyle": {},
            "emphasis": {"focus": "series"},
            "data": [820, 932, 901, 934, 1290, 1330, 1320],
        },
    ],
}
    st_echarts(options=options, height="300px", width="100%")



# Create a function to handle navigation between pages
def main():
    st.set_page_config(page_title="GEICO - Compliance", layout="wide", page_icon="g.png")

    # Create a sidebar for navigation
    pages = {
        "Home": main_page,
        "Policy Editor": yaml_editor_page,
        "Tagging": taggig,
        "Resources": resources,
        "Templates": template,
        "Help": help,
    }

    # Add tabs for each page
    st.sidebar.image("geico.png", use_column_width=True)
    current_page_name = st.sidebar.radio("Centralized Dashboard Policy and Compliance", list(pages.keys()))
    current_page = pages[current_page_name]

    # Display the selected page
    current_page()

if __name__ == "__main__":
    main()




# import streamlit as st
# from streamlit_echarts import st_echarts

# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "Welcome To GEICO",
#     ("Policy", "Administration", "Template")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Select Resource",
#         ("Tagged", "Untagged")
#     )
    
# options = {
#     "title": {"text": "Policy Compliance", "subtext": "GEICO", "left": "center"},
#     "tooltip": {"trigger": "item"},
#     "legend": {"orient": "vertical", "left": "left",},
#     "series": [
#         {
#             "name": "Usage",
#             "type": "pie",
#             "radius": "50%",
#             "data": [
#                 {"value": 1048, "name": "AWS"},
#                 {"value": 735, "name": "GCP"},
#                 {"value": 580, "name": "AZURE"},
#                 {"value": 484, "name": "ORACLE"},
#                 {"value": 300, "name": "IBM"},
#             ],
#             "emphasis": {
#                 "itemStyle": {
#                     "shadowBlur": 10,
#                     "shadowOffsetX": 0,
#                     "shadowColor": "rgba(0, 0, 0, 0.5)",
#                 }
#             },
#         }
#     ],
# }
# st_echarts(
#     options=options, height="600px",
# )
