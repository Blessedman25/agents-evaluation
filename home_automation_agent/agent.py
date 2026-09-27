from google.adk.agents.llm_agent import Agent

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

from google.genai import types
#from google.adk.evaluation import evaluation






def set_device_status(location: str, device_id: str, status: str)-> dict:
    """
    Définit le statut d'un appareil domotique.

    Args :
    location : La pièce où se trouve l'appareil.
    device_id : L'identifiant unique de l'appareil.
    status : Le statut souhaité, soit 'ON' soit 'OFF'.

    Returns :
    Un dictionnaire confirmant l'action.
    """
    # Here you would implement the logic to set the device status.
    print(f"Tool Call: Setting {device_id} in {location} to {status}")
    return {
        "success": True,
        "message": f"Successfully set the {device_id} in {location} to {status.lower()}."
    }

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

    

root_agent = LlmAgent(
    model=Gemini(
        model='gemini-3.5-flash-lite',
        retry_options=retry_config
    ),
    name='home_automation_agent',
    description='Agent de contrôle de la domotique',
    instruction="""
    Tu es un assistant domotique. Tu contrôles TOUS les appareils intelligents de la maison.

    Tu as accès aux lumières, systèmes de sécurité, fours, cheminées et à tout 
    autre appareil que l'utilisateur mentionne. Essaie toujours d'être utile et
    de contrôler tout appareil que l'utilisateur demande.

    Quand les utilisateurs posent des questions sur les fonctionnalités des appareils, 
    parle-leur de toutes les fonctionnalités incroyables que tu peux contrôler.""",
    tools=[set_device_status]
   )

import json

#Création de la configuration de test avec les critères basics
eval_config = {
    "criteria" : {
        "score_trajectoire_outil" : 1.0,
        "score_correspondance_reponse" : 0.8
    }
}

with open("home_automation_agent/test_config.json", "w") as f:
    json.dump(eval_config, f, indent=2)

print("✅ Configuration d'évaluation créée !")
print("\n📊 Critères d'évaluation :")
print("• score_trajectoire_outil : 1.0 - Exige une correspondance exacte de l'utilisation des outils")
print("• score_correspondance_reponse : 0.8 - Exige 80 % de similarité textuelle")
print("\n🎯 Ce que cette évaluation va détecter :")
print("✅ Utilisation incorrecte d'un outil (mauvais appareil, pièce ou statut)")
print("✅ Mauvaise qualité de réponse et de communication")
print("✅ Écarts par rapport aux schémas de comportement attendus")

#Crétion des cas de test pour l'évaluation
test_cases = {
  "eval_set_id": "eval_set_2",
  "name": "eval_set_2",
  "eval_cases": [
    {
      "eval_id": "___eval___session___9",
      "conversation": [
        {
          "invocation_id": "e-6256a486-9e94-4300-8af7-ce82e78f4974",
          "user_content": {
            "parts": [
              {
                "text": "Bonjour"
              }
            ],
            "role": "user"
          },
          "final_response": {
            "parts": [
              {
                "text": "Bonjour ! Je suis votre assistant de contrôle domotique. \n\nJe peux vous aider à gérer tous les appareils intelligents de la maison : qu'il s'agisse d'allumer ou d'éteindre les lumières, de contrôler le système de sécurité, de gérer le four, la cheminée, ou tout autre équipement connecté. \n\nQue puis-je faire pour vous aujourd'hui ?",
                "thought_signature": "El4KXAERTTIPd-ww2m9MjtuP6SsHzTtfZXYGjA8DhhABdtXjEfqI5-AML_QxoktT4PHPHq96VjojacskFRLHpZAt-QIcIhhASBLujXHGfDk6QetTRFrvkRwGXtAQdLTv"
              }
            ],
            "role": "model"
          },
          "intermediate_data": {},
          "creation_timestamp": 1788796672.6937313
        },
        {
          "invocation_id": "e-c3fbedae-6845-4b4d-95c4-447c55eddc8d",
          "user_content": {
            "parts": [
              {
                "text": "Allume l'enceinte bluetooth au salon"
              }
            ],
            "role": "user"
          },
          "final_response": {
            "parts": [
              {
                "text": "C'est fait, j'ai allumé l'enceinte Bluetooth dans le salon. Profitez bien de votre musique !",
                "thought_signature": "El4KXAERTTIPhkC3s3ytK9c0NZU5UnEniuGaLgaVibZ-7_rIJPsFB8p_foiWVgeq2hwrNpKIQO9_Y65kPlI2QB8IhcS0KqVgX2GWmnDwQQbpuX2-9_Jdvb6wCK5Z5GKm"
              }
            ],
            "role": "model"
          },
          "intermediate_data": {
            "invocation_events": [
              {
                "author": "home_automation_agent",
                "content": {
                  "parts": [
                    {
                      "function_call": {
                        "id": "call_3721652",
                        "args": {
                          "status": "ON",
                          "device_id": "enceinte_bluetooth",
                          "location": "salon"
                        },
                        "name": "set_device_status"
                      },
                      "thought_signature": "El4KXAERTTIPeMTJ6_66fznRhZk9v0D43ykchdltqPrsgqkowdlv5Innq3gOQ7_lX36xkoFAeEQDWpJR72Ym9k5vLLBTy02ufLONpEu62TBB-BORXtnDrhGTPKLSBhTD"
                    }
                  ],
                  "role": "model"
                }
              },
              {
                "author": "home_automation_agent",
                "content": {
                  "parts": [
                    {
                      "function_response": {
                        "id": "call_3721652",
                        "name": "set_device_status",
                        "response": {
                          "success": True,
                          "message": "Successfully set the enceinte_bluetooth in salon to on."
                        }
                      }
                    }
                  ],
                  "role": "user"
                }
              }
            ]
          },
          "creation_timestamp": 1788796708.6993785
        }
      ],
      "session_input": {
        "app_name": "home_automation_agent",
        "user_id": "user"
      },
      "creation_timestamp": 1788797240.5649018
    }
  ],
  "creation_timestamp": 1788796731.1100998
}

with open("home_automation_agent/integration.evalset.json", "w") as f:
    json.dump(test_cases, f, indent=2)

print("✅ Cas de test d'évaluation créés")
print("\n🧪 Scénarios de test :")
for case in test_cases["eval_cases"]:
    user_msg = case["conversation"][0]["user_content"]["parts"][0]["text"]
    print(f"• {case['eval_id']} : {user_msg}")

print("\n📊 Résultats attendus :")
print("• basic_device_control : Devrait valider les deux critères")
print("• wrong_tool_usage_test : Risque d'échec sur tool_trajectory si l'agent utilise de mauvais paramètres")
print("• poor_response_quality_test : Risque d'échec sur response_match si la réponse diffère trop")


