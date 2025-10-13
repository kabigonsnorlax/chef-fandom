# 🍳 Kabigon's Chef Fandom

A **web application** dedicated to tracking and visualizing the fandom communities of Thai chefs from **Heliconia H Group**’s competitive cooking shows and their **LINE Openchat** fan communities.

## 🌟 Overview

This application focuses on **chefs with established fandoms**, providing an organized and interactive way to explore fanbase trends across Thailand's TV show chefs competitions.

## 📊 Features

- **Multi-Show Coverage**: Supports all major Thai cooking competitions — *Hell’s Kitchen Thailand*, *Top Chef Thailand*, *MasterChef Thailand*, and *The Restaurant War*
- **Structured Presentation**: Displays chefs and competitors by show, sorted by relevance and display order
- **One-Click Access**: Instantly join fandoms via official LINE Openchat links

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **UI Framework**: Bootstrap 5
- **Data Format**: JSON
- **Hosting**: GitHub Pages
  
## 📁 Project Structure

```
chef-fandom/
├── index.html          # Main web application
├── data.json           # Chef data and fan counts
├── README.md           # Project documentation
├── count.py            # Fan count extraction utilities
└── images/             # Chef profile images
    ├── x.jpg
    ├── y.jpg
    └── ... (other chef images)
```
## 📊 Data Management

### Data Structure
Each chef entry contains:
- `GroupOrder`: Display order for cooking show groups
- `Group`: Cooking show name (e.g., "Hell's Kitchen Thailand")
- `Name`: Chef identifier (used for image filenames)
- `FullName`: Complete chef name in Thai
- `Kingdom`: Fandom/Openchat name
- `URL`: LINE Openchat invitation link
- `NameOrder`: Sorting order within groups
- `EstimateFans`: Current member count (auto-updated)


## 🔄 Automation

The project includes automated scripts for:
- Scraping live fan counts from LINE Openchat groups
- Data validation and error handling

Run the complete update process:
```bash
python count.py
```

## 🌐 Live Demo

Visit the live application at: [https://kabigonsnorlax.github.io/chef-fandom/](https://kabigonsnorlax.github.io/chef-fandom/)

## 🤝 Contributing

For issues, suggestions, or new chef additions, please contact via Facebook or create an issue on GitHub.

### Adding New Chefs / Competitors from Heliconia H Group
- Edit `data.json` directly to add new chef entries
- Include chef photo in `images/` folder (named as `{chef_name}.jpg`)
- Follow the existing JSON structure and naming conventions

## 📝 Notes

- **Disclaimer**: This project is not related to Heliconia H Group Company
- Fan counts are updated automatically every 5:00 and 17:00 daily
- Only active chefs with established fandoms are included
- All data is sourced from public LINE Openchat information

## 👨‍💻 Author

**Kabigon**
- Facebook: [just.kabigon](https://www.facebook.com/just.kabigon/)
- GitHub: [@kabigonsnorlax](https://github.com/kabigonsnorlax)

## 📄 License

This project is maintained by Kabigon for Cooking Show Community. Please respect the chefs and their fandom communities.