indexMapping = {
    "properties": {
        "ProductID": { 
            "type": "long" 
        },

        "ProductName": { 
            "type": "text" 
        },

        "ProductBrand": { 
            "type": "text" 
        },

        "Gender": { 
            "type": "text" 
        },

        "Price (INR)": { 
            "type": "long" 
        },

        "NumImages": { 
            "type": "long" 
        },

        "Description": { 
            "type": "text"  
        },

        "PrimaryColor": { 
            "type": "text" 
        },

        "DescriptionVector": {  # You can leave this as-is or set it later
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "l2_norm"
        }
    }
}