# 🎈 thl-open-data-2025

Code examples for the open data hackathon 2025 at TH Lübeck

### Apps

| App                      | Link |
| :----------------------- | :--- |
| Einwohner                | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://thl-open-data-2025-z7gxrtyvepkb8hpzg3qckh.streamlit.app) |
| Wasserstand (Vorlesung)  | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://thl-open-data-2025-6era47fek49vuqy5ecb9mb.streamlit.app) |
| Wasserstand (verbessert) | [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://thl-open-data-2025-jhjsaxrvahcq7xr5app6p63.streamlit.app) |

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run einwohner.py
   ```

   or

   ```
   $ streamlit run wasserstand_vorlesung.py
   ```

   or

   ```
   $ streamlit run wasserstand_verbessert.py
   ```

### How to deploy on Streamlit

1. Open repository in codespace
2. Commit and push your changes
3. [Create a Streamlit account](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/create-your-account). The easiest option is to use GitHub to sign up
4. [Connect your GitHub and Streamlit accounts](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/connect-your-github-account)
5. [Deploy your app on Streamlit](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy). Make sure to enter the right repository and file name
6. Done! :tada:
