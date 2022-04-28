PRODUCT_BLOCK_INDEX = 0
PROBLEM_BLOCK_INDEX = 2
SOLUTION_BLOCK_INDEX = 4

view = {
  "type": "modal",
  "title": {
    "type": "plain_text",
    "text": "New Knowladge Base Entry",
    "emoji": True
  },
  "private_metadata": "",
  "submit": {
    "type": "plain_text",
    "text": "Submit",
    "emoji": True
  },
  "close": {
    "type": "plain_text",
    "text": "Cancel",
    "emoji": True
  },
  "blocks": [
      {
        "block_id": "product",
        "type": "input",
        "element": {
          "type": "multi_static_select",
          "placeholder": {
            "type": "plain_text",
            "text": "Select one or more products",
            "emoji": True
          },
          "options": [],
          "action_id": "selected_product"
        },
        "label": {
          "type": "plain_text",
          "text": "Integrations Product",
          "emoji": True
        }
      },
      {
          "type": "divider"
      },
      {
        "block_id": "problem",
        "type": "input",
        "element": {
          "type": "plain_text_input",
          "multiline": True,
          "action_id": "problem_question",
          "initial_value": ""
      },
        "label": {
          "type": "plain_text",
          "text": "Problem / Question",
          "emoji": True
        }
      },
      {
        "type": "divider"
      },
      {
        "block_id": "solution",
        "type": "input",
        "element": {
            "type": "plain_text_input",
            "multiline": True,
            "action_id": "solution_response",
            "initial_value": ""
        },
        "label": {
            "type": "plain_text",
            "text": "Solution / Response",
            "emoji": True
        }
      }
  ]
}

def build_option(name, value):    
  return {
    "text": {
      "type": "plain_text",
      "text": name,
      "emoji": True
    },
    "value": value
  }

def build_view(data):
  options = [
    build_option('Bamboo Plugin', 'clm-bamboo-plugin'),
    build_option('IQ Azure DevOps', 'iq-azure-devops'),
    build_option('Jenkins Plugin', 'nexus-platform-plugin'),
    build_option('GitLab Plugin', 'gitlab-nexus-platform-plugin'),
    build_option('Maven Plugin', 'clm-maven-plugin'),
    build_option('IDEA Plugin', 'nexus-iq-idea-plugin'),
    build_option('Eclipse Plugin', 'insight-eclipse'),
    build_option('VS Plugin', 'nexus-visual-studio-plugin'),
    build_option('Native Nexus IQ CLI', 'native-image-nexus-iq-cli'),
    build_option('Docker Nexus IQ CLI', 'docker-nexus-iq-cli'),
    build_option('IQ Jira Plugin', 'iq-jira-plugin'),
    build_option('Helm Charts', 'helm3-charts'),
    build_option('Operators IQ', 'operators-iq'),
    build_option('Operators NXRM', 'operators-nxrm'),    
    build_option('Nexus Java API', 'nexus-java-api'),    
    build_option('Nexus SCM Client', 'nexus-scm-client'),    
    build_option('Other', 'other')
  ]

  view['private_metadata'] = data.metadata
  view['blocks'][PRODUCT_BLOCK_INDEX]['element']['options'] = options
  view['blocks'][PROBLEM_BLOCK_INDEX]['element']['initial_value'] = data.problem
  view['blocks'][SOLUTION_BLOCK_INDEX]['element']['initial_value'] = data.solution

  return view
