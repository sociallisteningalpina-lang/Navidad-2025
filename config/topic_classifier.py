#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable


def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para esta campaña.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("¿Dónde puedo comprar este producto?")
        # tema = 'Preguntas sobre el Producto'
    """
    
    def classify_topic(comment): 
        comment_lower = str(comment).lower()
    
    # Reacciones Positivas al Contenido
        if re.search(r'que bello|que lindo|gracias alpina|delicia|hermoso|bonito|precioso|me encanta|me gusta|linda|💕|🥰|😊|❤️', comment_lower):
            return 'Reacciones Positivas al Contenido'
    
    # Comentarios sobre IA/Autenticidad
        if re.search(r'\bia\b|inteligencia artificial|no es ia|que no es ia|auténtico|real', comment_lower):
            return 'Comentarios sobre IA/Autenticidad'
    
    # Preguntas sobre Recetas/Producto
        if re.search(r'c[oó]mo se prepara|qu[eé] ingredientes|mascarilla|receta|c[oó]mo hacer|explica|preparaci[oó]n|paso a paso', comment_lower):
            return 'Preguntas sobre Recetas/Producto'
    
    # Comentarios Religiosos/Bendiciones
        if re.search(r'bendiciones|am[eé]n|dios|gracias a dios|bendito|señor', comment_lower):
            return 'Comentarios Religiosos/Bendiciones'
    
    # Referencias a Personas Públicas/Figuras
        if re.search(r'zambrano|policía|aprovechado|ambicioso|verg[üu]enza|imagen personal|te ves', comment_lower):
            return 'Referencias a Personas/Off-topic'
    
    # Referencias Culturales/Memes
        if re.search(r'one piece|mapa|tinga linga|moradita|canciones|música', comment_lower):
            return 'Referencias Culturales/Memes'
    
    # Comentarios sobre Animales
        if re.search(r'perritos|perros|mascotas|animales|gatos', comment_lower):
            return 'Comentarios sobre Animales'
    
    # Menciones de Lugares
        if re.search(r'de la moradita|moradita|lugar|ciudad|pueblo', comment_lower):
            return 'Menciones de Lugares'
    
    # Fuera de Tema / No Relevante / Spam
        if re.search(r'listo|^\W*$|^[0-9]+$|^[a-z]{1,2}[0-9]+|pp099|hola\s*$', comment_lower) or len(comment_lower.split()) < 2:
            return 'Fuera de Tema / No Relevante'
    
        return 'Otros'
    return classify_topic

# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
