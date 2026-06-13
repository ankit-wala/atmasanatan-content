#!/usr/bin/env python3
"""
Create stub meta.yaml + en.md for every katha in the VS 2083 108-katha list.
Skips any folder that already exists (idempotent).
Run from repo root: python build/seed_stubs.py
"""

import os
import textwrap

BASE = os.path.join(os.path.dirname(__file__), "..", "kathas", "festivals")

# Each entry: slug, type, order, category, deity[], month, paksha, tithi,
#             region, tags[], sources[], title, scripture_ref
KATHAS = [
    # ── ASHADHA / July 2026 ──────────────────────────────────────────────────
    ("yogini-ekadashi",            "ekadashi", 1,  "major",
     ["Vishnu"],          "Ashadha",       "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","ashadha"],
     ["Padma Purana, Uttara Khanda — Sridhara katha",
      "DrikPanchang — Yogini Ekadashi"],
     "Yogini Ekadashi", "Padma Purana, Uttara Khanda"),

    ("jagannath-rath-yatra",       "festival", 2,  "major",
     ["Krishna","Jagannath"],      "Ashadha",       "Shukla",  "Dwitiya",
     "pan-india", ["rath-yatra","krishna","jagannath","ashadha"],
     ["Skanda Purana, Vaishnava Khanda — Indradyumna katha",
      "DrikPanchang — Jagannath Rath Yatra"],
     "Jagannath Rath Yatra", "Skanda Purana, Vaishnava Khanda"),

    ("devshayani-ekadashi",        "ekadashi", 3,  "major",
     ["Vishnu"],          "Ashadha",       "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","chaturmas","ashadha"],
     ["Brahma Vaivarta Purana — Vishnu enters yoganidra",
      "DrikPanchang — Devshayani Ekadashi"],
     "Devshayani Ekadashi — Chaturmas Aarambh",
     "Brahma Vaivarta Purana"),

    ("guru-purnima",               "festival", 4,  "major",
     ["Vyasa","Vishnu"],           "Ashadha",       "Shukla",  "Purnima",
     "pan-india", ["guru-purnima","vyasa","purnima","ashadha"],
     ["Mahabharata — Vyasa as adi-guru",
      "DrikPanchang — Guru Purnima"],
     "Guru Purnima — Vyas Puja", "Mahabharata, Adi Parva"),

    ("jaya-parvati-vrat",          "vrat",     5,  "minor",
     ["Shiva","Parvati"],          "Ashadha",       "Shukla",  "Panchami",
     "gujarat", ["vrat","shiva","parvati","ashadha","gujarat"],
     ["Skanda Purana — Jaya Parvati vrat katha",
      "DrikPanchang — Jaya Parvati Vrat"],
     "Jaya Parvati Vrat", "Skanda Purana"),

    # ── SHRAVAN / August 2026 ────────────────────────────────────────────────
    ("kamika-ekadashi",            "ekadashi", 6,  "major",
     ["Vishnu"],          "Shravan",       "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","shravan"],
     ["Brahma Vaivarta Purana — Kamika Ekadashi katha",
      "DrikPanchang — Kamika Ekadashi"],
     "Kamika Ekadashi", "Brahma Vaivarta Purana"),

    ("shravan-somvar-vrat",        "vrat",     7,  "major",
     ["Shiva"],           "Shravan",       "Shukla",  "Somvar",
     "pan-india", ["vrat","shiva","shravan","somvar","monday"],
     ["Skanda Purana — Shravan Somvar vrat katha",
      "DrikPanchang — Shravan Somvar"],
     "Shravan Somvar Vrat", "Skanda Purana"),

    ("solah-somvar-vrat",          "vrat",     8,  "major",
     ["Shiva"],           "Shravan",       "Shukla",  "Somvar",
     "pan-india", ["vrat","shiva","somvar","monday","solah-somvar"],
     ["Skanda Purana — Amravati / Vidyapati katha (16 Mondays)",
      "DrikPanchang — Solah Somvar Vrat"],
     "Solah Somvar Vrat", "Skanda Purana"),

    ("mangala-gauri-vrat",         "vrat",     9,  "major",
     ["Gauri","Parvati"],          "Shravan",       "Shukla",  "Mangalvar",
     "pan-india", ["vrat","gauri","parvati","shravan","tuesday"],
     ["Skanda Purana — Mangala Gauri vrat katha",
      "DrikPanchang — Mangala Gauri Vrat"],
     "Mangala Gauri Vrat", "Skanda Purana"),

    ("hariyali-teej",              "festival", 10, "major",
     ["Shiva","Parvati"],          "Shravan",       "Shukla",  "Tritiya",
     "pan-india", ["teej","shiva","parvati","shravan"],
     ["Shiva Purana — Shiva-Parvati reunion katha",
      "DrikPanchang — Hariyali Teej"],
     "Hariyali Teej", "Shiva Purana"),

    ("nag-panchami",               "festival", 11, "major",
     ["Nag","Shiva"],              "Shravan",       "Shukla",  "Panchami",
     "pan-india", ["nag-panchami","nag","shravan","snake"],
     ["Mahabharata, Adi Parva — Janmajeya yagya and Astika katha",
      "DrikPanchang — Nag Panchami"],
     "Nag Panchami", "Mahabharata, Adi Parva"),

    ("varalakshmi-vrat",           "vrat",     12, "major",
     ["Lakshmi","Vishnu"],         "Shravan",       "Shukla",  "Shukravar",
     "south-india", ["vrat","lakshmi","shravan","friday","south-india"],
     ["Skanda Purana — Charumati katha",
      "DrikPanchang — Varalakshmi Vrat"],
     "Varalakshmi Vrat", "Skanda Purana"),

    ("shravana-putrada-ekadashi",  "ekadashi", 13, "major",
     ["Vishnu"],          "Shravan",       "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","shravan","putrada"],
     ["Bhavishya Purana — King Mahijit katha",
      "DrikPanchang — Shravana Putrada Ekadashi"],
     "Shravana Putrada Ekadashi — King Mahijit ki Katha",
     "Bhavishya Purana"),

    ("raksha-bandhan",             "festival", 14, "major",
     ["Indra","Vishnu","Yama"],    "Shravan",       "Shukla",  "Purnima",
     "pan-india", ["raksha-bandhan","shravan","purnima","brother-sister"],
     ["Bhavishya Purana — Indra-Shachi katha",
      "DrikPanchang — Raksha Bandhan"],
     "Raksha Bandhan", "Bhavishya Purana"),

    ("kajari-teej",                "festival", 15, "minor",
     ["Shiva","Parvati"],          "Bhadrapada",    "Krishna", "Tritiya",
     "north-india", ["teej","shiva","parvati","bhadrapada"],
     ["Skanda Purana — Goddess Bhadra vrat katha",
      "DrikPanchang — Kajari Teej"],
     "Kajari Teej", "Skanda Purana"),

    # ── BHADRAPADA / September 2026 ──────────────────────────────────────────
    ("sheetala-satam",             "festival", 16, "major",
     ["Sheetala"],        "Bhadrapada",    "Krishna", "Saptami",
     "gujarat", ["sheetala","bhadrapada","gujarat","cold-food","randhan-chhath"],
     ["Skanda Purana — Sheetala Mata katha",
      "DrikPanchang — Sheetala Saptami"],
     "Sheetala Satam — Randhan Chhath", "Skanda Purana"),

    ("hal-shashthi",               "festival", 17, "minor",
     ["Balarama"],        "Bhadrapada",    "Krishna", "Shashthi",
     "north-india", ["hal-shashthi","balarama","bhadrapada"],
     ["Vishnu Purana — Balarama katha",
      "DrikPanchang — Hal Shashthi / Balarama Jayanti"],
     "Hal Shashthi — Balarama Jayanti", "Vishnu Purana"),

    ("janmashtami",                "festival", 18, "major",
     ["Krishna"],         "Bhadrapada",    "Krishna", "Ashtami",
     "pan-india", ["janmashtami","krishna","bhadrapada","birth"],
     ["Bhagavata Purana, Skandha 10, Ch. 1-3 — Krishna janma, Devaki-Kansa arc, transfer to Gokul",
      "DrikPanchang — Janmashtami"],
     "Janmashtami — Shri Krishna Janma",
     "Bhagavata Purana, Skandha 10"),

    ("aja-ekadashi",               "ekadashi", 19, "major",
     ["Vishnu"],          "Bhadrapada",    "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","bhadrapada"],
     ["Brahma Vaivarta Purana — King Harishchandra katha",
      "DrikPanchang — Aja Ekadashi"],
     "Aja Ekadashi — Harishchandra ki Katha", "Brahma Vaivarta Purana"),

    ("hartalika-teej",             "festival", 20, "major",
     ["Shiva","Parvati"],          "Bhadrapada",    "Shukla",  "Tritiya",
     "pan-india", ["teej","shiva","parvati","bhadrapada","vrat"],
     ["Shiva Purana — Parvati's austerity and Shiva-Parvati vivah katha",
      "DrikPanchang — Hartalika Teej"],
     "Hartalika Teej — Parvati ki Tapasya", "Shiva Purana"),

    ("ganesh-chaturthi-janma",     "festival", 21, "major",
     ["Ganesha"],         "Bhadrapada",    "Shukla",  "Chaturthi",
     "pan-india", ["ganesh-chaturthi","ganesha","bhadrapada","birth"],
     ["Shiva Purana, Rudra Samhita — Ganesha janma katha",
      "DrikPanchang — Ganesh Chaturthi"],
     "Ganesh Chaturthi — Ganesha Janma Katha",
     "Shiva Purana, Rudra Samhita"),

    ("ganesh-chaturthi-syamantaka","festival", 22, "major",
     ["Ganesha","Krishna"],        "Bhadrapada",    "Shukla",  "Chaturthi",
     "pan-india", ["ganesh-chaturthi","ganesha","syamantaka","moon-curse"],
     ["Bhagavata Purana, Skandha 10 — Syamantaka Mani katha (why moon is not seen on Chaturthi)",
      "DrikPanchang — Ganesh Chaturthi"],
     "Ganesh Chaturthi — Syamantaka Mani aur Chandrama ka Shrap",
     "Bhagavata Purana, Skandha 10"),

    ("rishi-panchami",             "festival", 23, "minor",
     ["Saptarishi"],      "Bhadrapada",    "Shukla",  "Panchami",
     "pan-india", ["rishi-panchami","saptarishi","bhadrapada","vrat"],
     ["Bhavishya Purana — Saptarishi vrat, Arundhati katha",
      "DrikPanchang — Rishi Panchami"],
     "Rishi Panchami — Saptarishi Vrat", "Bhavishya Purana"),

    ("radha-ashtami",              "festival", 24, "major",
     ["Radha","Krishna"],          "Bhadrapada",    "Shukla",  "Ashtami",
     "pan-india", ["radha-ashtami","radha","krishna","bhadrapada"],
     ["Brahma Vaivarta Purana, Prakriti Khanda — Radha janma katha",
      "DrikPanchang — Radha Ashtami"],
     "Radha Ashtami — Shri Radha Janma",
     "Brahma Vaivarta Purana, Prakriti Khanda"),

    ("parivartini-ekadashi",       "ekadashi", 25, "major",
     ["Vishnu"],          "Bhadrapada",    "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","bhadrapada","parsva"],
     ["Brahma Vaivarta Purana — Vishnu turns sides in yoganidra",
      "DrikPanchang — Parivartini / Parsva Ekadashi"],
     "Parivartini Ekadashi — Vishnu Karwat Lekar Baithte Hain",
     "Brahma Vaivarta Purana"),

    ("vamana-jayanti",             "festival", 26, "major",
     ["Vamana","Vishnu","Bali"],   "Bhadrapada",    "Shukla",  "Dwadashi",
     "pan-india", ["vamana","vishnu","bali","onam","bhadrapada"],
     ["Bhagavata Purana, Skandha 8, Ch. 15-23 — Bali-Vamana katha",
      "DrikPanchang — Vamana Jayanti"],
     "Vamana Jayanti — Bali aur Teen Paon Zameen",
     "Bhagavata Purana, Skandha 8"),

    ("anant-chaturdashi",          "festival", 27, "major",
     ["Vishnu","Ananta"],          "Bhadrapada",    "Shukla",  "Chaturdashi",
     "pan-india", ["anant-chaturdashi","vishnu","ananta","bhadrapada"],
     ["Skanda Purana — Kaundinya aur Sushila katha",
      "DrikPanchang — Anant Chaturdashi"],
     "Anant Chaturdashi — Anant Vrat Katha", "Skanda Purana"),

    # ── ASHWIN / October 2026 ────────────────────────────────────────────────
    ("mahalaya-pitru-paksha",      "festival", 28, "major",
     ["Pitru","Yama"],             "Ashwin",        "Krishna", "Amavasya",
     "pan-india", ["mahalaya","pitru-paksha","shraddha","ashwin","karna"],
     ["Mahabharata — Karna's shraddha katha (why he gives gold in afterlife)",
      "DrikPanchang — Mahalaya Amavasya / Sarva Pitru Amavasya"],
     "Mahalaya — Pitru Paksha aur Karna ki Katha", "Mahabharata"),

    ("jivitputrika",               "vrat",     29, "major",
     ["Jivit","Surya"],            "Ashwin",        "Krishna", "Ashtami",
     "east-india", ["jivitputrika","jitiya","vrat","ashwin","son"],
     ["Skanda Purana — Jimutavahana katha",
      "DrikPanchang — Jivitputrika / Jitiya Vrat"],
     "Jivitputrika Vrat — Jimutavahana ki Katha", "Skanda Purana"),

    ("indira-ekadashi",            "ekadashi", 30, "major",
     ["Vishnu"],          "Ashwin",        "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","ashwin","pitru"],
     ["Brahma Vaivarta Purana — Indrasena / ancestor liberation katha",
      "DrikPanchang — Indira Ekadashi"],
     "Indira Ekadashi — Pitra Mukti katha", "Brahma Vaivarta Purana"),

    ("navratri-shailputri",        "festival", 31, "major",
     ["Shailputri","Durga"],       "Ashwin",        "Shukla",  "Pratipada",
     "pan-india", ["navratri","durga","shailputri","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Shailputri swaroop",
      "DrikPanchang — Sharad Navratri Day 1"],
     "Navratri Day 1 — Maa Shailputri", "Markandeya Purana, Devi Mahatmya"),

    ("navratri-brahmacharini",     "festival", 32, "major",
     ["Brahmacharini","Durga"],    "Ashwin",        "Shukla",  "Dwitiya",
     "pan-india", ["navratri","durga","brahmacharini","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Brahmacharini swaroop",
      "DrikPanchang — Sharad Navratri Day 2"],
     "Navratri Day 2 — Maa Brahmacharini",
     "Markandeya Purana, Devi Mahatmya"),

    ("navratri-chandraghanta",     "festival", 33, "major",
     ["Chandraghanta","Durga"],    "Ashwin",        "Shukla",  "Tritiya",
     "pan-india", ["navratri","durga","chandraghanta","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Chandraghanta swaroop",
      "DrikPanchang — Sharad Navratri Day 3"],
     "Navratri Day 3 — Maa Chandraghanta",
     "Markandeya Purana, Devi Mahatmya"),

    ("navratri-kushmanda",         "festival", 34, "major",
     ["Kushmanda","Durga"],        "Ashwin",        "Shukla",  "Chaturthi",
     "pan-india", ["navratri","durga","kushmanda","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Kushmanda swaroop",
      "DrikPanchang — Sharad Navratri Day 4"],
     "Navratri Day 4 — Maa Kushmanda",
     "Markandeya Purana, Devi Mahatmya"),

    ("navratri-skandamata",        "festival", 35, "major",
     ["Skandamata","Durga"],       "Ashwin",        "Shukla",  "Panchami",
     "pan-india", ["navratri","durga","skandamata","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Skandamata swaroop",
      "DrikPanchang — Sharad Navratri Day 5"],
     "Navratri Day 5 — Maa Skandamata",
     "Markandeya Purana, Devi Mahatmya"),

    ("navratri-katyayani",         "festival", 36, "major",
     ["Katyayani","Durga"],        "Ashwin",        "Shukla",  "Shashthi",
     "pan-india", ["navratri","durga","katyayani","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Katyayani swaroop",
      "DrikPanchang — Sharad Navratri Day 6"],
     "Navratri Day 6 — Maa Katyayani",
     "Markandeya Purana, Devi Mahatmya"),

    ("navratri-kalaratri",         "festival", 37, "major",
     ["Kalaratri","Durga"],        "Ashwin",        "Shukla",  "Saptami",
     "pan-india", ["navratri","durga","kalaratri","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Kalaratri swaroop",
      "DrikPanchang — Sharad Navratri Day 7"],
     "Navratri Day 7 — Maa Kalaratri",
     "Markandeya Purana, Devi Mahatmya"),

    ("navratri-mahagauri",         "festival", 38, "major",
     ["Mahagauri","Durga"],        "Ashwin",        "Shukla",  "Ashtami",
     "pan-india", ["navratri","durga","mahagauri","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Mahagauri swaroop",
      "DrikPanchang — Sharad Navratri Day 8"],
     "Navratri Day 8 — Maa Mahagauri",
     "Markandeya Purana, Devi Mahatmya"),

    ("navratri-siddhidatri",       "festival", 39, "major",
     ["Siddhidatri","Durga"],      "Ashwin",        "Shukla",  "Navami",
     "pan-india", ["navratri","durga","siddhidatri","ashwin"],
     ["Markandeya Purana, Devi Mahatmya — Siddhidatri swaroop",
      "DrikPanchang — Sharad Navratri Day 9"],
     "Navratri Day 9 — Maa Siddhidatri",
     "Markandeya Purana, Devi Mahatmya"),

    ("vijayadashami",              "festival", 40, "major",
     ["Rama","Durga"],             "Ashwin",        "Shukla",  "Dashami",
     "pan-india", ["vijayadashami","dussehra","rama","ashwin","aparajita"],
     ["Valmiki Ramayana — Rama's victory over Ravana",
      "DrikPanchang — Vijayadashami / Dussehra"],
     "Vijayadashami — Asatya par Satya ki Vijay", "Valmiki Ramayana"),

    ("papankusha-ekadashi",        "ekadashi", 41, "major",
     ["Vishnu"],          "Ashwin",        "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","ashwin"],
     ["Brahma Vaivarta Purana — Papankusha katha",
      "DrikPanchang — Papankusha Ekadashi"],
     "Papankusha Ekadashi", "Brahma Vaivarta Purana"),

    ("sharad-purnima",             "festival", 42, "major",
     ["Lakshmi","Krishna"],        "Ashwin",        "Shukla",  "Purnima",
     "pan-india", ["sharad-purnima","kojagari","lakshmi","ashwin","moon"],
     ["Devi Bhagavata Purana — Lakshmi's night walk katha",
      "DrikPanchang — Sharad Purnima / Kojagari"],
     "Sharad Purnima — Kojagari Lakshmi Puja", "Devi Bhagavata Purana"),

    ("karwa-chauth",               "vrat",     43, "major",
     ["Shiva","Parvati","Kartikeya"], "Kartik",     "Krishna", "Chaturthi",
     "north-india", ["karwa-chauth","vrat","kartik","married-women"],
     ["Skanda Purana — Veeravati katha",
      "DrikPanchang — Karwa Chauth"],
     "Karwa Chauth — Veeravati ki Katha", "Skanda Purana"),

    # ── KARTIK / November 2026 ────────────────────────────────────────────────
    ("ahoi-ashtami",               "vrat",     44, "major",
     ["Ahoi Mata"],       "Kartik",        "Krishna", "Ashtami",
     "north-india", ["ahoi-ashtami","vrat","kartik","mother","son"],
     ["Folk tradition — Ahoi Mata vrat katha (oral tradition, no single Puranic source)",
      "DrikPanchang — Ahoi Ashtami"],
     "Ahoi Ashtami", "Folk tradition (oral)"),

    ("rama-ekadashi",              "ekadashi", 45, "major",
     ["Vishnu"],          "Kartik",        "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","kartik"],
     ["Brahma Vaivarta Purana — Rama Ekadashi katha",
      "DrikPanchang — Rama Ekadashi"],
     "Rama Ekadashi", "Brahma Vaivarta Purana"),

    ("govatsa-dwadashi",           "festival", 46, "minor",
     ["Krishna","Cow"],            "Kartik",        "Krishna", "Dwadashi",
     "pan-india", ["govatsa","vasu-baras","cow","kartik","krishna"],
     ["Skanda Purana — Govatsa / Vasu Baras katha",
      "DrikPanchang — Govatsa Dwadashi / Vasu Baras"],
     "Govatsa Dwadashi — Vasu Baras", "Skanda Purana"),

    ("dhanteras",                  "festival", 47, "major",
     ["Dhanvantari","Lakshmi","Yama"], "Kartik",    "Krishna", "Trayodashi",
     "pan-india", ["dhanteras","dhanvantari","lakshmi","kartik","diwali"],
     ["Bhagavata Purana, Skandha 8 — Dhanvantari janma (samudra manthan)",
      "Skanda Purana — King Hima's son katha",
      "DrikPanchang — Dhanteras"],
     "Dhanteras — Dhanvantari aur King Hima ke Putra ki Katha",
     "Bhagavata Purana, Skandha 8"),

    ("narak-chaturdashi",          "festival", 48, "major",
     ["Krishna","Narakasura"],     "Kartik",        "Krishna", "Chaturdashi",
     "pan-india", ["narak-chaturdashi","kali-chaudas","krishna","narakasura","kartik"],
     ["Bhagavata Purana, Skandha 10 — Narakasura vadh katha",
      "DrikPanchang — Narak Chaturdashi / Kali Chaudas"],
     "Narak Chaturdashi — Narakasura Vadh", "Bhagavata Purana, Skandha 10"),

    # ORDER 49 = diwali — already exists, skip creation

    ("govardhan-puja",             "festival", 50, "major",
     ["Krishna","Govardhan"],      "Kartik",        "Shukla",  "Pratipada",
     "pan-india", ["govardhan","krishna","annakut","kartik","diwali"],
     ["Bhagavata Purana, Skandha 10 — Govardhan Dhari Krishna lila",
      "DrikPanchang — Govardhan Puja / Annakut"],
     "Govardhan Puja — Giriraj Dhari Krishna", "Bhagavata Purana, Skandha 10"),

    ("bhai-dooj",                  "festival", 51, "major",
     ["Yama","Yamuna"],            "Kartik",        "Shukla",  "Dwitiya",
     "pan-india", ["bhai-dooj","yama-dwitiya","yama","yamuna","kartik"],
     ["Skanda Purana — Yama visits Yamuna katha",
      "DrikPanchang — Bhai Dooj / Yama Dwitiya"],
     "Bhai Dooj — Yama aur Yamuna", "Skanda Purana"),

    ("chitragupta-puja",           "festival", 52, "minor",
     ["Chitragupta","Yama"],       "Kartik",        "Shukla",  "Dwitiya",
     "pan-india", ["chitragupta","yama","kartik","kayastha"],
     ["Padma Purana — Chitragupta's creation katha",
      "DrikPanchang — Chitragupta Puja"],
     "Chitragupta Puja — Yama ke Lekhpal ki Katha", "Padma Purana"),

    ("chhath-puja",                "festival", 53, "major",
     ["Surya","Chhathi Maiya"],    "Kartik",        "Shukla",  "Shashthi",
     "north-india", ["chhath","surya","shashthi","kartik","bihar","up"],
     ["Skanda Purana — Draupadi / Priyavrata Surya katha",
      "DrikPanchang — Chhath Puja / Surya Shashthi"],
     "Chhath Puja — Surya Shashthi Vrat",
     "Skanda Purana / Vishnu Purana"),

    ("skanda-shashthi",            "festival", 54, "major",
     ["Kartikeya","Skanda"],       "Kartik",        "Shukla",  "Shashthi",
     "south-india", ["skanda-shashthi","kartikeya","soorasamharam","kartik"],
     ["Skanda Purana — Kartikeya vadh of Surapadman",
      "DrikPanchang — Skanda Shashthi"],
     "Skanda Shashthi — Soorasamharam", "Skanda Purana"),

    ("gopashtami",                 "festival", 55, "minor",
     ["Krishna","Cow"],            "Kartik",        "Shukla",  "Ashtami",
     "pan-india", ["gopashtami","krishna","cow","kartik"],
     ["Bhagavata Purana, Skandha 10 — Krishna becomes cowherd katha",
      "DrikPanchang — Gopashtami"],
     "Gopashtami — Krishna Bane Gwalbal",
     "Bhagavata Purana, Skandha 10"),

    ("akshaya-navami",             "festival", 56, "minor",
     ["Vishnu","Amla"],            "Kartik",        "Shukla",  "Navami",
     "pan-india", ["akshaya-navami","amla-navami","vishnu","kartik","amla"],
     ["Skanda Purana — Amla tree and Vishnu katha",
      "DrikPanchang — Akshaya Navami / Amla Navami"],
     "Akshaya Navami — Amla aur Vishnu ki Katha", "Skanda Purana"),

    ("devutthana-ekadashi",        "ekadashi", 57, "major",
     ["Vishnu"],          "Kartik",        "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","kartik","dev-prabodhini","chaturmas-end"],
     ["Brahma Vaivarta Purana — Vishnu wakes from yoganidra",
      "DrikPanchang — Devutthana / Dev Prabodhini Ekadashi"],
     "Devutthana Ekadashi — Vishnu Uthte Hain", "Brahma Vaivarta Purana"),

    ("tulsi-vivah",                "festival", 58, "major",
     ["Vishnu","Tulsi","Vrinda"],  "Kartik",        "Shukla",  "Dwadashi",
     "pan-india", ["tulsi-vivah","vishnu","tulsi","vrinda","jalandhara","kartik"],
     ["Padma Purana, Uttara Khanda — Vrinda-Jalandhara-Vishnu katha",
      "DrikPanchang — Tulsi Vivah"],
     "Tulsi Vivah — Vrinda aur Vishnu ki Katha",
     "Padma Purana, Uttara Khanda"),

    ("dev-diwali",                 "festival", 59, "major",
     ["Shiva","Tripurasura"],      "Kartik",        "Shukla",  "Purnima",
     "pan-india", ["dev-diwali","kartik-purnima","shiva","tripurasura","varanasi"],
     ["Shiva Purana — Tripurasura vadh katha",
      "DrikPanchang — Dev Diwali / Kartik Purnima"],
     "Dev Diwali — Tripurasura Vadh aur Devon ki Diwali",
     "Shiva Purana"),

    # ── MARGASHIRSHA / December 2026 ─────────────────────────────────────────
    ("kalabhairav-jayanti",        "festival", 60, "minor",
     ["Bhairava","Shiva"],         "Margashirsha",  "Krishna", "Ashtami",
     "pan-india", ["kalabhairav","bhairava","shiva","margashirsha"],
     ["Shiva Purana — Kala Bhairava's appearance from Shiva",
      "DrikPanchang — Kalabhairav Jayanti"],
     "Kalabhairav Jayanti", "Shiva Purana"),

    ("utpanna-ekadashi",           "ekadashi", 61, "major",
     ["Vishnu","Ekadashi Devi"],   "Margashirsha",  "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","margashirsha","ekadashi-devi-birth"],
     ["Padma Purana — Birth of Ekadashi Devi from Vishnu",
      "DrikPanchang — Utpanna Ekadashi"],
     "Utpanna Ekadashi — Ekadashi Devi ka Prakatya",
     "Padma Purana"),

    ("vivah-panchami",             "festival", 62, "major",
     ["Rama","Sita"],              "Margashirsha",  "Shukla",  "Panchami",
     "pan-india", ["vivah-panchami","rama","sita","margashirsha","marriage"],
     ["Valmiki Ramayana, Bala Kanda — Rama-Sita vivah katha",
      "DrikPanchang — Vivah Panchami"],
     "Vivah Panchami — Shri Ram aur Sita ka Vivah",
     "Valmiki Ramayana, Bala Kanda"),

    ("champa-shashthi",            "festival", 63, "minor",
     ["Khandoba","Shiva"],         "Margashirsha",  "Shukla",  "Shashthi",
     "maharashtra", ["champa-shashthi","khandoba","shiva","margashirsha","maharashtra"],
     ["Skanda Purana — Khandoba katha (Maharashtra regional)",
      "DrikPanchang — Champa Shashthi"],
     "Champa Shashthi — Khandoba Maharaj ki Katha", "Skanda Purana"),

    ("mokshada-ekadashi",          "ekadashi", 64, "major",
     ["Vishnu","Gita"],            "Margashirsha",  "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","gita-jayanti","margashirsha","moksha"],
     ["Brahma Vaivarta Purana — Mokshada Ekadashi katha",
      "Mahabharata, Bhishma Parva — Gita Jayanti context",
      "DrikPanchang — Mokshada Ekadashi / Gita Jayanti"],
     "Mokshada Ekadashi — Gita Jayanti", "Brahma Vaivarta Purana"),

    ("dattatreya-jayanti",         "festival", 65, "minor",
     ["Dattatreya","Brahma","Vishnu","Shiva"], "Margashirsha", "Shukla", "Purnima",
     "pan-india", ["dattatreya","trimurti","margashirsha","purnima"],
     ["Devi Bhagavata Purana — Dattatreya birth from Atri-Anasuya",
      "DrikPanchang — Dattatreya Jayanti"],
     "Dattatreya Jayanti — Atri aur Anusuya ki Katha",
     "Devi Bhagavata Purana"),

    # ── PAUSHA / January 2027 ────────────────────────────────────────────────
    ("saphala-ekadashi",           "ekadashi", 66, "major",
     ["Vishnu"],          "Pausha",        "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","pausha"],
     ["Brahma Vaivarta Purana — Lumpaka / Kalimasa katha",
      "DrikPanchang — Saphala Ekadashi"],
     "Saphala Ekadashi", "Brahma Vaivarta Purana"),

    ("makar-sankranti",            "festival", 67, "major",
     ["Surya","Shani"],            "Pausha",        "Shukla",  "Sankranti",
     "pan-india", ["makar-sankranti","surya","shani","uttarayan","pongal","lohri"],
     ["Bhavishya Purana — Surya-Shani reconciliation katha",
      "Mahabharata — Bhishma's choice of death on Uttarayan",
      "DrikPanchang — Makar Sankranti"],
     "Makar Sankranti — Uttarayan aur Surya-Shani Katha",
     "Bhavishya Purana / Mahabharata"),

    ("pausha-putrada-ekadashi",    "ekadashi", 68, "major",
     ["Vishnu"],          "Pausha",        "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","pausha","putrada"],
     ["Bhavishya Purana — King Suketuman katha (distinct from Shravana Putrada)",
      "DrikPanchang — Pausha Putrada Ekadashi"],
     "Pausha Putrada Ekadashi — Raja Suketuman ki Katha",
     "Bhavishya Purana"),

    ("sakat-chauth",               "vrat",     69, "major",
     ["Ganesha"],         "Pausha",        "Krishna", "Chaturthi",
     "north-india", ["sakat-chauth","ganesha","pausha","chaturthi","son","vrat"],
     ["Folk tradition / Skanda Purana — Sakat Mata vrat katha",
      "DrikPanchang — Sakat Chauth"],
     "Sakat Chauth — Putra ki Raksha", "Skanda Purana (folk tradition)"),

    ("shakambhari-purnima",        "festival", 70, "minor",
     ["Shakambhari","Devi"],       "Pausha",        "Shukla",  "Purnima",
     "pan-india", ["shakambhari","devi","pausha","purnima"],
     ["Devi Bhagavata Purana — Shakambhari Devi katha",
      "DrikPanchang — Shakambhari Purnima"],
     "Shakambhari Purnima", "Devi Bhagavata Purana"),

    # ── MAGHA / February 2027 ────────────────────────────────────────────────
    ("shattila-ekadashi",          "ekadashi", 71, "major",
     ["Vishnu"],          "Magha",         "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","magha","tildaan"],
     ["Padma Purana — Til-daan (sesame gift) katha",
      "DrikPanchang — Shattila Ekadashi"],
     "Shattila Ekadashi — Til ke Daan ki Mahima", "Padma Purana"),

    ("mauni-amavasya",             "festival", 72, "minor",
     ["Ganga","Shiva"],            "Magha",         "Krishna", "Amavasya",
     "pan-india", ["mauni-amavasya","ganga","snan","magha","mauna"],
     ["Padma Purana — Magha snan and mauna vrat significance",
      "DrikPanchang — Mauni Amavasya"],
     "Mauni Amavasya — Maun aur Ganga Snan", "Padma Purana"),

    ("vasant-panchami",            "festival", 73, "major",
     ["Saraswati"],       "Magha",         "Shukla",  "Panchami",
     "pan-india", ["vasant-panchami","saraswati","magha","basant","spring"],
     ["Devi Bhagavata Purana — Saraswati's manifestation katha",
      "DrikPanchang — Vasant Panchami"],
     "Vasant Panchami — Maa Saraswati ka Prakatya",
     "Devi Bhagavata Purana"),

    ("ratha-saptami",              "festival", 74, "minor",
     ["Surya"],           "Magha",         "Shukla",  "Saptami",
     "pan-india", ["ratha-saptami","surya","magha","chariot"],
     ["Bhavishya Purana — Surya's chariot and Yashovarma katha",
      "DrikPanchang — Ratha Saptami"],
     "Ratha Saptami — Surya ka Rath", "Bhavishya Purana"),

    ("bhishma-ashtami",            "festival", 75, "minor",
     ["Bhishma","Vishnu"],         "Magha",         "Shukla",  "Ashtami",
     "pan-india", ["bhishma-ashtami","bhishma","magha","mahabharata"],
     ["Mahabharata, Anushasana Parva — Bhishma's departure on Uttarayan",
      "DrikPanchang — Bhishma Ashtami"],
     "Bhishma Ashtami — Pitamah ka Swarga Prayan", "Mahabharata"),

    ("jaya-ekadashi",              "ekadashi", 76, "major",
     ["Vishnu"],          "Magha",         "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","magha","apsara"],
     ["Padma Purana — Pushpavat / Apsara liberation katha",
      "DrikPanchang — Jaya Ekadashi"],
     "Jaya Ekadashi — Apsara ki Mukti", "Padma Purana"),

    ("magha-purnima",              "festival", 77, "minor",
     ["Vishnu","Ganga"],           "Magha",         "Shukla",  "Purnima",
     "pan-india", ["magha-purnima","ganga","snan","vishnu","magha"],
     ["Padma Purana — Magha snan Mahatmya katha",
      "DrikPanchang — Magha Purnima"],
     "Magha Purnima — Snan aur Daan ki Mahima", "Padma Purana"),

    # ── PHALGUNA / March 2027 ────────────────────────────────────────────────
    ("vijaya-ekadashi",            "ekadashi", 78, "major",
     ["Vishnu"],          "Phalguna",      "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","phalguna"],
     ["Brahma Vaivarta Purana — Vasudeva-Dharmaraj katha",
      "DrikPanchang — Vijaya Ekadashi"],
     "Vijaya Ekadashi", "Brahma Vaivarta Purana"),

    ("maha-shivaratri",            "festival", 79, "major",
     ["Shiva","Parvati"],          "Phalguna",      "Krishna", "Chaturdashi",
     "pan-india", ["maha-shivaratri","shiva","phalguna","hunter","lingodbhava"],
     ["Skanda Purana — Lubdhaka the hunter vrat katha",
      "Shiva Purana — Lingodbhava / Shiva-Parvati vivah",
      "DrikPanchang — Maha Shivaratri"],
     "Maha Shivaratri — Lubdhak aur Shiv ki Katha", "Skanda Purana"),

    ("amalaki-ekadashi",           "ekadashi", 80, "major",
     ["Vishnu"],          "Phalguna",      "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","phalguna","amla"],
     ["Brahma Vaivarta Purana — Vaishya Chandramati katha",
      "DrikPanchang — Amalaki Ekadashi"],
     "Amalaki Ekadashi — Amla aur Moksha", "Brahma Vaivarta Purana"),

    ("holika-dahan",               "festival", 81, "major",
     ["Vishnu","Prahlada","Holika"], "Phalguna",    "Shukla",  "Purnima",
     "pan-india", ["holika-dahan","prahlada","hiranyakashipu","vishnu","phalguna"],
     ["Bhagavata Purana, Skandha 7 — Prahlada-Hiranyakashipu katha",
      "DrikPanchang — Holika Dahan"],
     "Holika Dahan — Prahlad ki Bhakti aur Holika ki Katha",
     "Bhagavata Purana, Skandha 7"),

    ("sheetala-ashtami",           "festival", 82, "minor",
     ["Sheetala"],        "Chaitra",       "Krishna", "Ashtami",
     "north-india", ["sheetala-ashtami","sheetala","chaitra","cold-food","north-india"],
     ["Skanda Purana — Sheetala Mata katha (North India Chaitra version)",
      "DrikPanchang — Sheetala Ashtami"],
     "Sheetala Ashtami — Basoda Puja",
     "Skanda Purana"),

    # ── CHAITRA / April 2027 ─────────────────────────────────────────────────
    ("papmochani-ekadashi",        "ekadashi", 83, "major",
     ["Vishnu"],          "Chaitra",       "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","chaitra"],
     ["Brahma Vaivarta Purana — Muni Medhavi katha",
      "DrikPanchang — Papmochani Ekadashi"],
     "Papmochani Ekadashi — Medhavi Muni ki Katha",
     "Brahma Vaivarta Purana"),

    ("gangaur",                    "festival", 84, "major",
     ["Gauri","Shiva"],            "Chaitra",       "Shukla",  "Tritiya",
     "rajasthan", ["gangaur","gauri","shiva","chaitra","rajasthan","mp"],
     ["Skanda Purana — Isara-Gauri katha",
      "DrikPanchang — Gangaur"],
     "Gangaur — Isara aur Gauri ki Prem Katha", "Skanda Purana"),

    ("ram-navami",                 "festival", 85, "major",
     ["Rama","Sita"],              "Chaitra",       "Shukla",  "Navami",
     "pan-india", ["ram-navami","rama","chaitra","birth","ayodhya"],
     ["Valmiki Ramayana, Bala Kanda — Rama janma katha",
      "DrikPanchang — Ram Navami"],
     "Ram Navami — Shri Rama Janma",
     "Valmiki Ramayana, Bala Kanda"),

    ("kamada-ekadashi",            "ekadashi", 86, "major",
     ["Vishnu"],          "Chaitra",       "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","chaitra"],
     ["Brahma Vaivarta Purana — Lalitha-Lalit katha",
      "DrikPanchang — Kamada Ekadashi"],
     "Kamada Ekadashi — Lalitha aur Lalit", "Brahma Vaivarta Purana"),

    ("hanuman-jayanti",            "festival", 87, "major",
     ["Hanuman"],         "Chaitra",       "Shukla",  "Purnima",
     "pan-india", ["hanuman-jayanti","hanuman","chaitra","purnima","birth"],
     ["Valmiki Ramayana — Hanuman janma katha",
      "DrikPanchang — Hanuman Jayanti"],
     "Hanuman Jayanti — Pawanputra Hanuman ka Janm",
     "Valmiki Ramayana"),

    # ── VAISHAKHA / May 2027 ─────────────────────────────────────────────────
    ("varuthini-ekadashi",         "ekadashi", 88, "major",
     ["Vishnu"],          "Vaishakha",     "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","vaishakha"],
     ["Brahma Vaivarta Purana — Mandhata katha",
      "DrikPanchang — Varuthini Ekadashi"],
     "Varuthini Ekadashi — Raja Mandhata ki Katha",
     "Brahma Vaivarta Purana"),

    ("akshaya-tritiya",            "festival", 89, "major",
     ["Vishnu","Lakshmi","Kubera"],"Vaishakha",     "Shukla",  "Tritiya",
     "pan-india", ["akshaya-tritiya","vishnu","sudama","akshaya-patra","vaishakha"],
     ["Mahabharata — Sudama katha / Akshaya Patra katha",
      "DrikPanchang — Akshaya Tritiya"],
     "Akshaya Tritiya — Sudama aur Akshaya Patra",
     "Mahabharata / Bhagavata Purana"),

    ("parashurama-jayanti",        "festival", 90, "major",
     ["Parashurama","Vishnu"],     "Vaishakha",     "Shukla",  "Tritiya",
     "pan-india", ["parashurama","vishnu","avatar","vaishakha"],
     ["Bhagavata Purana / Vishnu Purana — Parashurama avatar katha",
      "DrikPanchang — Parashurama Jayanti"],
     "Parashurama Jayanti — Parashurama Avatar",
     "Bhagavata Purana"),

    ("sita-navami",                "festival", 91, "minor",
     ["Sita","Rama"],              "Vaishakha",     "Shukla",  "Navami",
     "pan-india", ["sita-navami","sita","rama","vaishakha","janaka"],
     ["Valmiki Ramayana — Sita janma katha (Janaka finds Sita in furrow)",
      "DrikPanchang — Sita Navami"],
     "Sita Navami — Maa Sita ka Prakatya",
     "Valmiki Ramayana"),

    ("mohini-ekadashi",            "ekadashi", 92, "major",
     ["Vishnu"],          "Vaishakha",     "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","vaishakha"],
     ["Brahma Vaivarta Purana — Dhrishtabuddhi katha",
      "DrikPanchang — Mohini Ekadashi"],
     "Mohini Ekadashi — Dhrishtabuddhi ki Katha", "Brahma Vaivarta Purana"),

    ("narasimha-jayanti",          "festival", 93, "major",
     ["Narasimha","Vishnu","Prahlada"], "Vaishakha", "Shukla",  "Chaturdashi",
     "pan-india", ["narasimha","vishnu","prahlada","hiranyakashipu","vaishakha"],
     ["Bhagavata Purana, Skandha 7 — Hiranyakashipu vadh / Narasimha avatar",
      "DrikPanchang — Narasimha Jayanti"],
     "Narasimha Jayanti — Hiranyakashipu Vadh",
     "Bhagavata Purana, Skandha 7"),

    ("buddha-purnima",             "festival", 94, "minor",
     ["Buddha","Vishnu","Kurma"],  "Vaishakha",     "Shukla",  "Purnima",
     "pan-india", ["buddha-purnima","kurma-jayanti","vishnu","vaishakha","purnima"],
     ["Bhagavata Purana, Skandha 8 — Kurma avatar (samudra manthan) katha",
      "DrikPanchang — Buddha Purnima / Kurma Jayanti"],
     "Buddha Purnima — Kurma Jayanti aur Samudra Manthan",
     "Bhagavata Purana, Skandha 8"),

    # ── JYESHTHA / June 2027 ────────────────────────────────────────────────
    ("apara-ekadashi",             "ekadashi", 95, "major",
     ["Vishnu"],          "Jyeshtha",      "Krishna", "Ekadashi",
     "pan-india", ["ekadashi","vishnu","jyeshtha"],
     ["Brahma Vaivarta Purana — Mahidhvaja katha",
      "DrikPanchang — Apara Ekadashi"],
     "Apara Ekadashi — Mahidhvaja ki Katha", "Brahma Vaivarta Purana"),

    ("vat-savitri-vrat",           "vrat",     96, "major",
     ["Savitri","Satyavan","Yama"],"Jyeshtha",      "Krishna", "Amavasya",
     "pan-india", ["vat-savitri","savitri","satyavan","yama","jyeshtha","vrat"],
     ["Mahabharata, Vana Parva, Ch. 293-299 — Savitri-Satyavan katha",
      "DrikPanchang — Vat Savitri Vrat"],
     "Vat Savitri Vrat — Savitri aur Satyavan",
     "Mahabharata, Vana Parva"),

    ("shani-jayanti",              "festival", 97, "major",
     ["Shani","Surya"],            "Jyeshtha",      "Krishna", "Amavasya",
     "pan-india", ["shani-jayanti","shani","surya","chhaya","jyeshtha"],
     ["Brahma Purana — Shani's birth from Surya-Chhaya",
      "DrikPanchang — Shani Jayanti"],
     "Shani Jayanti — Surya Putra Shani ka Janm", "Brahma Purana"),

    ("ganga-dussehra",             "festival", 98, "major",
     ["Ganga","Shiva"],            "Jyeshtha",      "Shukla",  "Dashami",
     "pan-india", ["ganga-dussehra","ganga","bhagiratha","shiva","jyeshtha"],
     ["Valmiki Ramayana, Bala Kanda, Ch. 43-44 — Bhagiratha's tapasya",
      "Bhagavata Purana, Skandha 9 — Ganga's descent to earth",
      "DrikPanchang — Ganga Dussehra"],
     "Ganga Dussehra — Bhagiratha ki Tapasya aur Ganga ka Avtaran",
     "Valmiki Ramayana, Bala Kanda"),

    ("nirjala-ekadashi",           "ekadashi", 99, "major",
     ["Vishnu"],          "Jyeshtha",      "Shukla",  "Ekadashi",
     "pan-india", ["ekadashi","vishnu","jyeshtha","nirjala","bhima"],
     ["Brahma Vaivarta Purana — Bhima's waterless fast (Vyasa advises Bhima)",
      "DrikPanchang — Nirjala Ekadashi"],
     "Nirjala Ekadashi — Bhima ki Nirajal Tapasya",
     "Brahma Vaivarta Purana"),

    # ── SATYANARAYAN KATHA (5 adhyayas, placed on Purnimas) ─────────────────
    ("satyanarayan-adhyaya-1",     "vrat",    100, "major",
     ["Vishnu","Satyanarayan"],    "Shravan",       "Shukla",  "Purnima",
     "pan-india", ["satyanarayan","vishnu","purnima","adhyaya"],
     ["Skanda Purana, Reva Khanda, Ch. 1 — Saunaka-Suta frame, Brahmin katha"],
     "Satyanarayan Katha — Adhyaya 1 (Brahmin ki Katha)",
     "Skanda Purana, Reva Khanda"),

    ("satyanarayan-adhyaya-2",     "vrat",    101, "major",
     ["Vishnu","Satyanarayan"],    "Kartik",        "Shukla",  "Purnima",
     "pan-india", ["satyanarayan","vishnu","purnima","adhyaya","woodcutter"],
     ["Skanda Purana, Reva Khanda, Ch. 2 — Lakdahara (woodcutter) katha"],
     "Satyanarayan Katha — Adhyaya 2 (Lakadhare ki Katha)",
     "Skanda Purana, Reva Khanda"),

    ("satyanarayan-adhyaya-3",     "vrat",    102, "major",
     ["Vishnu","Satyanarayan"],    "Margashirsha",  "Shukla",  "Purnima",
     "pan-india", ["satyanarayan","vishnu","purnima","adhyaya","merchant"],
     ["Skanda Purana, Reva Khanda, Ch. 3 — Sadhu Vania aur Kalavati katha"],
     "Satyanarayan Katha — Adhyaya 3 (Sadhu Vania ki Katha)",
     "Skanda Purana, Reva Khanda"),

    ("satyanarayan-adhyaya-4",     "vrat",    103, "major",
     ["Vishnu","Satyanarayan"],    "Magha",         "Shukla",  "Purnima",
     "pan-india", ["satyanarayan","vishnu","purnima","adhyaya","king"],
     ["Skanda Purana, Reva Khanda, Ch. 4 — King Tungadhwaja katha"],
     "Satyanarayan Katha — Adhyaya 4 (Raja Tungadhwaja ki Katha)",
     "Skanda Purana, Reva Khanda"),

    ("satyanarayan-adhyaya-5",     "vrat",    104, "major",
     ["Vishnu","Satyanarayan"],    "Vaishakha",     "Shukla",  "Purnima",
     "pan-india", ["satyanarayan","vishnu","purnima","adhyaya"],
     ["Skanda Purana, Reva Khanda, Ch. 5 — Phalashruti (phala of the vrat)"],
     "Satyanarayan Katha — Adhyaya 5 (Phalashruti)",
     "Skanda Purana, Reva Khanda"),

    # ── WEEKDAY VRAT KATHAS (floating, most popular 4) ──────────────────────
    ("somvar-vrat",                "vrat",    105, "minor",
     ["Shiva"],           "Shravan",       "Shukla",  "Somvar",
     "pan-india", ["somvar","monday","shiva","vrat","weekday"],
     ["Skanda Purana — Somvar vrat katha (general; distinct from Shravan Somvar)",
      "DrikPanchang — Somvar Vrat"],
     "Somvar Vrat — Shiv ki Aradhana",
     "Skanda Purana (folk tradition)"),

    ("mangalvar-vrat",             "vrat",    106, "minor",
     ["Hanuman","Mangal"],         "Bhadrapada",    "Shukla",  "Mangalvar",
     "pan-india", ["mangalvar","tuesday","hanuman","mangal","vrat","weekday"],
     ["Folk tradition — Mangalvar vrat katha"],
     "Mangalvar Vrat — Mangalmurti ki Aradhana",
     "Folk tradition (oral)"),

    ("shukravar-santoshi",         "vrat",    107, "major",
     ["Santoshi Mata"],            "Ashwin",        "Shukla",  "Shukravar",
     "pan-india", ["santoshi-mata","friday","shukravar","vrat","weekday"],
     ["Folk tradition — Santoshi Mata vrat katha (20th c. oral tradition; no Puranic source)"],
     "Santoshi Mata Vrat — Shukravar ki Katha",
     "Folk tradition (oral, 20th century)"),

    ("shanivar-vrat",              "vrat",    108, "minor",
     ["Shani"],           "Margashirsha",  "Krishna", "Shanivar",
     "pan-india", ["shanivar","saturday","shani","vrat","weekday"],
     ["Skanda Purana / folk — Shanivar vrat katha",
      "DrikPanchang — Shani Vrat"],
     "Shanivar Vrat — Shani Dev ki Aradhana",
     "Skanda Purana (folk tradition)"),
]


META_TEMPLATE = """\
slug: {slug}
type: {type}
order: {order}
category: {category}
deity:
{deity_lines}
panchang:
  month: {month}
  paksha: {paksha}
  tithi: {tithi}
  date_2026: TODO-VERIFY   # YYYY-MM-DD — verify against DrikPanchang before publishing
  date_2027: TODO-VERIFY   # second occurrence; same katha, different date
region: {region}
related_shlokas: []
related_bhajans: []
tags:
{tag_lines}
sources:
{source_lines}
scripture_ref: "{scripture_ref}"
status: draft
"""

EN_TEMPLATE = """\
---
slug: {slug}
lang: en
title: "{title}"
subtitle: "TODO"
summary: "TODO — one to two sentences."
reel_hook: "TODO — scroll-stopping question."
---

## Katha

TODO — tell the story. Source: {scripture_ref}

## Significance

TODO — spiritual and cultural meaning.

## Vidhi

TODO — puja / vrat steps in order.

## Observance

TODO — fasting rules, timing, parana. (Required for vrats; optional for festivals.)

## Mantras

TODO — key shloka in Devanagari + transliteration + one-line meaning.
"""


def write_stub(entry):
    (slug, etype, order, category, deity, month, paksha, tithi,
     region, tags, sources, title, scripture_ref) = entry

    folder = os.path.join(BASE, slug)
    if os.path.exists(folder):
        print(f"  SKIP  {slug}  (already exists)")
        return

    os.makedirs(folder)

    deity_lines = "\n".join(f"  - {d}" for d in deity)
    tag_lines   = "\n".join(f"  - {t}" for t in tags)
    source_lines= "\n".join(f'  - "{s}"' for s in sources)

    meta = META_TEMPLATE.format(
        slug=slug, type=etype, order=order, category=category,
        deity_lines=deity_lines, month=month, paksha=paksha, tithi=tithi,
        region=region, tag_lines=tag_lines, source_lines=source_lines,
        scripture_ref=scripture_ref,
    )
    en = EN_TEMPLATE.format(slug=slug, title=title, scripture_ref=scripture_ref)

    with open(os.path.join(folder, "meta.yaml"), "w") as f:
        f.write(meta)
    with open(os.path.join(folder, "en.md"), "w") as f:
        f.write(en)

    print(f"  CREATE {order:>3}  {slug}")


if __name__ == "__main__":
    print(f"Seeding stubs into {BASE}\n")
    for entry in KATHAS:
        write_stub(entry)
    print(f"\nDone. {len(KATHAS)} entries processed.")
    print("Also updating diwali order to 49…")
    # Patch diwali order in meta.yaml
    diwali_meta = os.path.join(BASE, "diwali", "meta.yaml")
    if os.path.exists(diwali_meta):
        with open(diwali_meta) as f:
            text = f.read()
        text = text.replace("order: 100", "order: 49")
        with open(diwali_meta, "w") as f:
            f.write(text)
        print("  PATCH  diwali  order → 49")
