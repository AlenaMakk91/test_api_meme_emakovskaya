default_post_payload = {
    "text": "Лучший способ выучить язык - это общаться с его носителем. Программисты на питоне:",
    "url": "https://cvam.ru/wp-content/uploads/2023/09/garri-potter-programmist-1.webp",
    "tags": [
        "python",
        "garri-potter",
        "programmist"
    ],
    "info": {
        "color": [
            "white",
            "grey",
            "brown"
        ]
    }
}

payload_without_text = {
    "url": "https://cvam.ru/wp-content/uploads/2023/09/garri-potter-programmist-1.webp",
    "tags": [
        "python",
        "garri-potter",
        "programmist"
    ],
    "info": {
        "color": [
            "white",
            "grey",
            "brown"
        ]
    }
}

payload_without_url = {
    "text": "Лучший способ выучить язык - это общаться с его носителем. Программисты на питоне:",
    "tags": [
        "python",
        "garri-potter",
        "programmist"
    ],
    "info": {
        "color": [
            "white",
            "grey",
            "brown"
        ]
    }
}

payload_without_tags = {
    "text": "Лучший способ выучить язык - это общаться с его носителем. Программисты на питоне:",
    "url": "https://cvam.ru/wp-content/uploads/2023/09/garri-potter-programmist-1.webp",
    "info": {
        "color": [
            "white",
            "grey",
            "brown"
        ]
    }
}

payload_without_info = {
    "text": "Лучший способ выучить язык - это общаться с его носителем. Программисты на питоне:",
    "url": "https://cvam.ru/wp-content/uploads/2023/09/garri-potter-programmist-1.webp",
    "tags": [
        "python",
        "garri-potter",
        "programmist"
    ]
}

payload_with_empty_body = {}

payload_incorrect_type_for_text = {
    "text": 123,
    "url": "https://cvam.ru/wp-content/uploads/2023/09/garri-potter-programmist-1.webp",
    "tags": [
        "python",
        "garri-potter",
        "programmist"
    ],
    "info": {
        "color": [
            "white",
            "grey",
            "brown"
        ]
    }
}

payload_incorrect_type_for_tags = {
    "text": "Лучший способ выучить язык - это общаться с его носителем. Программисты на питоне:",
    "url": "https://cvam.ru/wp-content/uploads/2023/09/garri-potter-programmist-1.webp",
    "tags": {
        "python": 123
    },
    "info": {
        "color": [
            "white",
            "grey",
            "brown"
        ]
    }
}

payload_incorrect_type_for_url = {
    "text": "Лучший способ выучить язык - это общаться с его носителем. Программисты на питоне:",
    "url": 123,
    "tags": [
        "python",
        "garri-potter",
        "programmist"
    ],
    "info": {
        "color": [
            "white",
            "grey",
            "brown"
        ]
    }
}

payload_incorrect_type_for_info = {
    "text": "Лучший способ выучить язык - это общаться с его носителем. Программисты на питоне:",
    "url": "https://cvam.ru/wp-content/uploads/2023/09/garri-potter-programmist-1.webp",
    "tags": [
        "python",
        "garri-potter",
        "programmist"
    ],
    "info":
        [
            "white",
            "grey",
            "brown"
        ]

}
