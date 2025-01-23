import freenect
import numpy as np
import cv2
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO)

def get_depth():
    """Récupère les données de profondeur depuis le capteur Kinect."""
    try:
        depth, _ = freenect.sync_get_depth()
        if depth is None:
            logging.error("Impossible de récupérer les données de profondeur.")
            return None
        return depth
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des données de profondeur : {e}")
        return None

def normalize_depth(depth):
    """Normalise les données de profondeur pour les adapter à une colormap."""
    depth = np.clip(depth, 0, 2047)  # Limite les valeurs à l'intervalle utile
    depth_normalized = (depth / 2047.0 * 255).astype(np.uint8)  # Normalise pour 8 bits
    return depth_normalized

def main():
    logging.info("Démarrage de la capture vidéo.")
    try:
        while True:
            # Récupération des données de profondeur
            depth = get_depth()
            if depth is None:
                continue

            # Normalisation des données
            depth_normalized = normalize_depth(depth)

            # Application de la colormap
            depth_colored = cv2.applyColorMap(depth_normalized, cv2.COLORMAP_TURBO)

            # Affichage
            cv2.imshow("Vue de profondeur", depth_colored)

            # Gestion des événements clavier
            if cv2.waitKey(1) & 0xFF == ord('q'):
                logging.info("Fermeture de la fenêtre demandée par l'utilisateur.")
                break

    except KeyboardInterrupt:
        logging.info("Interruption par l'utilisateur.")
    finally:
        # Libération des ressources
        cv2.destroyAllWindows()
        logging.info("Fenêtre fermée et mémoire libérée.")

if __name__ == "__main__":
    main()

