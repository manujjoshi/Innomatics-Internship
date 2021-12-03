import streamlit as st


from PIL import Image


add_selectbox = st.sidebar.selectbox(
"You can navigate to ",('Home', 'About','Certifications','Work Experience','Projects','Resume','Contact'))

if add_selectbox == 'Home':
    st.title('Home Page')
    image = Image.open('F:\Important Documents\My Pics\m.jfif')
    st.image(image, caption='Manuj Kumar Joshi')
    st.header('Hello! Thank You for taking the time to view my Portfolio. This webapp was built using Streamlit, a Python Library.')
elif add_selectbox == 'About':
    st.title('About page')
    
    st.header('An aspiring Data Scientist pursuing his data science training at Innomatics Research Labs, Hyderabad. I have completed my Computer Science Engineering in 2014.')
    st.header('Below are a few highlights of my life:')
    st.subheader('22 Oct 1992')
    st.markdown('I Took Avatar in India :birthday:')
    st.subheader('May 2008')
    st.markdown('Cleared my 10th :prince:')
    st.subheader('May 2010')
    st.markdown('Cleared my 12th :prince:')
    st.subheader('May 2014')
    st.markdown('Cleared my graduation :prince:')
    st.subheader('Dec 2014')
    st.markdown('Diagonosed with Multiple Sclerosis, doctor deported to home for recovery :pill: :calendar:')
    st.subheader('Oct 2020')
    st.markdown('Started preparing for Data Science to rejuvenate my career :fire:')
    st.subheader('Mar 2021')
    st.markdown('Did a one month intership at TSF as Data Science & Business Analytics Intern :fire:')
    st.subheader('April 2021')
    st.markdown('Did a one month intership at TSF as IOT & CV Intern, made COVID mask Detector :fire:')
    st.subheader('May 2021')
    st.markdown('Started Data Science Training at Innomatics Research Labs, Hyderabad :fire:')
    st.subheader('July 2021')
    st.markdown('Completed my Data Science Specilization course from EICT Academy, IIT Roorkee :fire:')
    st.subheader('Oct 2021')
    st.markdown('Started Internship at Innomatics Research Labs as Data Science intern :fire:')

elif add_selectbox == 'Work Experience':
    st.title('Work Experience Page')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Data Science Intern at Innomatics Research Labs')
    st.subheader('May 2021 - Present , Hyderabad(Remote)')
    st.write('1. I worked here in Innomatics in May 2021. Although initially it was challenging, I believe I adapted well to the situation.')
    st.write('2. Here I worked on many machine learning models eg. regression, classification and unsupervised.')
    st.write('3. Here I worked on many deep learning models.')
    st.write('4. Along with modelling I also learn productionization of models.')
    st.write('5. Here I learnt many front end tools such as HTML, CSS, Bootstrap.')
    st.write('6. Here I learnt many backend tools such as Flask, streamlit.')
    st.write('7. Here I also worked on  databases theough SQLAlchemy.')
    st.write('8. Made 2 Major Projects and prepared reports')
    st.write(":heavy_minus_sign:" * 34)
    st.header('IOT and Computer vision intern at TSF')
    st.subheader('April 2021 - June 2021, Singapore(Remote)')
    st.write('1. Here I made a COVID-19 mask detector.')
    st.write('2. It tells that a user has wored mask or not, It use to detect mask and flask on screen that a user has wore mask or not.')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Data Science and Business Analytics Intern at TSF')
    st.subheader('March 2021 - April 2021, Singapore(Remote)')
    st.write('1. Here I work2d on many datasets, 2 regression, 2 classifcation, 2 unspervised,2 business cases and one dashboard preparation.')
    st.write('2. Here I learnt how to deal with a dataset to present insights to a customer which can help him to increase sales.')
    st.write('3. Here I dealt regression problems and predicted numerical labels.')
    st.write('4. Here I dealt classification problems and predicted categorical labels.')
    st.write('5. Here I dealt unsupervised problems and cluster similar observations.')

elif add_selectbox == 'Projects':
    st.title('Projects Page')
    st.write(":heavy_minus_sign:" * 34)
    st.header('URL shortner')
    st.subheader('Oct 2021')
    st.write('1. Made a URL Shortener that shorten the original URL, through that shorten URLthe user will be re-directed to the original URL page.')
    st.write('2. Used Flask for the back end along with HTML and CSS for the front end and SQLAlchemy for the data base purpose.')
    st.write('3. When the user press submit button, through the POST request the data is transmitted to the backend where it is shortened, along with that, original URL with its shortened URL is stored in the Data Base.')
    st.write('4. Through that shortened URL the user will be re-directed to the original URL and the same shorten URL can also be use in future for re-direction.')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Web Scraping')
    st.subheader('Aug 2021')
    st.write('1. Scrapped an automobile website, and extracted bike and cars data to do data analysis to suggested the vehicle to the customer as per his budget and specifications.')
    st.write('2. Scrapped the website with the help BeautifulSoup.')
    st.write('3. Presented a Power Point presentation to the customer.')
    st.write(":heavy_minus_sign:" * 34)
    st.header('COVID-19 Mask Detector with help of Deep Learning.')
    st.subheader('April 2021')
    st.write('Designed COVID-19 Mask Detector which detect that the user is with mask or not and show a warning if he’s without mask.')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Data Analysis and Machine Learning')
    st.subheader('March 2021')
    st.write('Worked on multiple datasets to do Descriptive Analysis, Diagnostic Analytics, Predictive analysis and Prescriptive Analysis.')
    st.write('Used the patterns to predict response with help Regression, Classification and Clustering Algorithms.')
elif add_selectbox == 'Contact':
    st.title('Contact page')
    st.header('Email:')
    link = '[Email](https:/manujjoshi52@gmail.com)'
    st.markdown(link, unsafe_allow_html=True,)
    st.header('Contact no:')
    st.markdown('+91-9557287321')

    st.header('LinkedIn:')
    link = '[LinkedIn](https://www.linkedin.com/in/manuj-kumar-joshi-036148197/)'
    st.markdown(link, unsafe_allow_html=True)

    st.header('Github:')
    link = '[Github](https://github.com/manujjoshi)'
    st.markdown(link, unsafe_allow_html=True)
    
    st.header('Address:')
    st.text('Nainital,Uttrakhand')


elif add_selectbox == 'Resume':
    st.title('Resume Page')
    image1 = Image.open('F:\Important Documents\My Pics\Manuj\m1.jfif')
    st.image(image1, caption='Page 1')
    image2 = Image.open('F:\Important Documents\My Pics\Manuj\m2.jpg')
    st.image(image2, caption='Page 2')
    

elif add_selectbox == 'Certifications':
    st.title('Certifications Page')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Data Science Professional from Innomatics Research Labs, Hyderabad')
    st.write('Course module covers Python, SQL, Statistics, Machine Learning, Deep Learning, Computer vision, NLP and Productionization of models.')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Data Science Specialization from EICT Academy IIT Roorkee')
    st.write('Course module Big Data Analytics, Machine Learning and Deep Learning.')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Python 101, Data Visualization, Data Analytics, ML and DL from Cognitive class with IBM Badge')
    st.write(":heavy_minus_sign:" * 34)
    st.header('Excel Crash Course: Spreadsheet Formulas for Finance from Corporate Finance Institute, Canada.')
    st.write(":heavy_minus_sign:" * 34)
    st.header('LinkedIn Certified in Python')