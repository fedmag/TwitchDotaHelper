#%%
import json

class Parser:
    """
    Class used to parse the file containing heroes and abilities.
    
    The class returns a dictionary like: { hero_name: [ability1, ...] }
    The ability is represented as follows:
    "ability_name $ ability_description".

    Attributes
    ----------
    filepath: str
        indicates the path from which the file must be read
    hero_dict: dict
        the dictionary that will be populated and then returned

    Methods
    ---------
    parse_file(filepath)
        main method that calls all the others and provides the end-to-end job
    clean_ability_descp_pair(line, hero_name)
        takes the line and extrapolate the ability given the hero name, ignoring useless lines given words
        appearing in the line
    clean_ability_name(line, hero_name)
        takes the line like: "DOTA_Tooltip_ability_templar_assassin_trap_Description" and gives back "trap"
    get_dictionary
        a dictionary like: { hero_name: [ability1, ...] }
    get_dictionary_JSON
        returns the hero_dictionary as a JSON string
    hero_dict_to_file(filepath):
        Write the json to a file

    """
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.hero_dict = {}

    def parse_file(self):
        """
        main method that calls all the others and provides the end-to-end job

        """
        with open (self.filepath, 'r') as file:
            hero_name = None
            ability_list = []
            for line in file:
                if "//" in line and len(line) <25: # heroes name are always preceeded by //, unfortunately also other lines
                    self.hero_dict[hero_name] = ability_list
                    ability_list = []
                    hero_name = line[4:].lower().strip()
                else:
                    cleaned_sentence = self.clean_ability_descp_pair(line, hero_name)
                    if cleaned_sentence != None:
                        ability_list.append(cleaned_sentence) 

    def clean_ability_descp_pair(self, line: str, hero_name: str) -> str:
        """ 
        Takes a line and extrapolate the ability given the hero name, ignoring useless lines 
        given words appearing in the line 

        Parameters
        ----------
        line: str
            line to clean
        hero_name: str
            the eroe associated with the line

        Returns
        -------
        dict
            dictionary: { "ability_name" : "ability_description" }

        """

        tokens = line.split("\"")
        if (len(tokens) > 3 and "Description" in tokens[1] and
            "ability" in tokens[1] and "aghanim" not in tokens[1] and
            "item" not in tokens[1] and "special" not in tokens[1] and 
            "stop" not in tokens[1] and "release" not in tokens[1] and
            "Grants new ability" not in tokens[-2]
            ): # the goal line contains "ability" and "description", but not  "special", "item" or "aghanim" TODO: aghs can be implemented
            ability_name = self.clean_ability_name(tokens[1], hero_name) # FIXME: must be cleaned
            ability_descr = tokens[-2]
            ability_descr_pair = { ability_name : ability_descr }
            return ability_descr_pair

    def clean_ability_name(self, line: str, hero_name: str) -> str:
        """
        Takes a line like: "DOTA_Tooltip_ability_templar_assassin_trap_Description" and gives back "trap" 

        Parameters
        ----------
        line: str
            line to clean
        hero_name: str
            the eroe associated with the line
        
        Returns
        -------
        str
            the name of the ability
        """

        # there are a seriese of inconsistencies in the data regarding the names: sometime they are splitted like "queen of pain" but in the ability it s represente as "queenofpain"

        line = line.replace("_", " ")
        tokens = line.split(" ")
        hero_name = self.check_for_name_inconsistencies(hero_name)
        name_splits = hero_name.split(" ")
        ability_name = tokens[3 + len(name_splits): -1]
        ability_name = " ".join(ability_name) 
        return ability_name

    def check_for_name_inconsistencies(self, name: str) -> str:
        if name == "queen of pain":
            return "queenofpain"
        if name == "blood seeker":
            return "bloodseeker"
        if name == "centaur warchief":
            return "centaur"
        if name == "treant protector":
            return "treant"
        if name == "shadowshaman":
            return "shadowshaman"
        if name == "witchdoctor":
            return "witch doctor"
        # if name == "Outworld Devourer":
        #     return "obsidian destroyer"

            
        else: 
            return name

    def get_dictionary(self) -> dict:
        """ 
        Returns
        -------
        dict
            a dictionary like: { hero_name: [ability1, ...] }
        """
        return self.hero_dict

    def get_dictionary_JSON(self) -> str:
        """
        Returns
        -------
        str
            a str representing a JSON of a dictionary like: { hero_name: [ability1, ...] }
        """
        return json.dumps(self.hero_dict)

    def hero_dict_to_file(self, filepath):
        """ 
        Write the json to a file

        Parameters
        ----------
        filepath: str
            the path to the new file
        
        """
        with open (filepath, 'w') as file:
            file.write(self.get_dictionary_JSON())
            print("File successfully created!")

    
parser = Parser("data/abilitiesRaw.txt")
parser.parse_file()
parser.hero_dict_to_file("src/js/heroes_dict_with_dict.json")


# %%
