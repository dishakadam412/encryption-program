{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNRubsyidww5J8XEO7M56MK",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dishakadam412/encryption-program/blob/main/encryption_program.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cSMTSW_eLwAR",
        "outputId": "27800c65-7e38-4f32-9750-27eb2cbe5e8b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "What message would you like to encrypt? : pizza\n",
            "original message : pizza\n",
            "encrypted message : IH<<>\n",
            "What message would you like to decrypt? : IH<<>\n",
            "encrypted message : IH<<>\n",
            "original message : pizza\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "import string\n",
        "\n",
        "## Makes a list of characters\n",
        "## then copies and shuffles it to encrypt the word\n",
        "\n",
        "chars = \" \" + string.punctuation + string.digits + string.ascii_letters\n",
        "chars = list(chars)\n",
        "key = chars.copy()\n",
        "\n",
        "random.shuffle(key)\n",
        "\n",
        "## Asks user for message to encrypt\n",
        "## then it will find a letter at the index and replace it in the cipher text\n",
        "\n",
        "plain_text = input(\"What message would you like to encrypt? : \")\n",
        "cipher_text = \"\"\n",
        "\n",
        "for letter in plain_text:\n",
        "  index = chars.index(letter)\n",
        "  cipher_text += key[index]\n",
        "\n",
        "## Displays original msg and encrypted msg\n",
        "\n",
        "print(f\"original message : {plain_text}\")\n",
        "print(f\"encrypted message : {cipher_text}\")\n",
        "\n",
        "## ---- Decryption ----\n",
        "\n",
        "cipher_text = input(\"What message would you like to decrypt? : \")\n",
        "plain_text = \"\"\n",
        "\n",
        "for letter in cipher_text:\n",
        "  index = key.index(letter)\n",
        "  plain_text += chars[index]\n",
        "\n",
        "print(f\"encrypted message : {cipher_text}\")\n",
        "print(f\"original message : {plain_text}\")"
      ]
    }
  ]
}