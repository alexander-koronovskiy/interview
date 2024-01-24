import cv2
import numpy as np
from numba import njit


def fast_glcm(img, vmin=0, vmax=255, nbit=8):
    mi, ma = vmin, vmax
    h, w = img.shape

    # digitize
    bins = np.linspace(mi, ma + 1, nbit + 1)
    gl1 = np.digitize(img, bins) - 1
    gl2 = np.append(gl1[:, 1:], gl1[:, -1:], axis=1)

    # make glcm
    glcm = np.zeros((nbit, nbit, h, w), dtype=np.uint8)
    for i in range(nbit):
        for j in range(nbit):
            mask = ((gl1 == i) & (gl2 == j))
            glcm[i, j, mask] = 1

    kernel = np.ones((5, 5), dtype=np.uint8)
    for i in range(nbit):
        for j in range(nbit):
            glcm[i, j] = cv2.filter2D(glcm[i, j], -1, kernel)
    return glcm.astype(np.float32)


@njit
def fast_glcm_mean(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm mean
    """
    _, nbit, h, w = glcm.shape
    mean = np.zeros((h, w), dtype=np.float32)
    for i in range(nbit):
        for j in range(nbit):
            mean += glcm[i,j] * i / nbit ** 2
    return mean


@njit
def fast_glcm_std(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm std
    """
    _, nbit, h, w = glcm.shape
    mean = fast_glcm_mean(glcm)
    std2 = np.zeros((h, w), dtype=np.float32)
    for i in range(nbit):
        for j in range(nbit):
            std2 += (glcm[i, j] * i - mean) ** 2

    return np.sqrt(std2)


@njit
def fast_glcm_contrast(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm contrast
    """
    _, nbit, h, w = glcm.shape
    cont = np.zeros((h, w), dtype=np.float32)
    for i in range(nbit):
        for j in range(nbit):
            cont += glcm[i, j] * (i - j) ** 2
    return cont


@njit
def fast_glcm_dissimilarity(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm dissimilarity
    """
    _, nbit, h, w = glcm.shape
    diss = np.zeros((h, w), dtype=np.float32)
    for i in range(nbit):
        for j in range(nbit):
            diss += glcm[i, j] * np.abs(i - j)
    return diss


@njit
def fast_glcm_homogeneity(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm homogeneity
    """
    _, nbit, h, w = glcm.shape
    homo = np.zeros((h, w), dtype=np.float32)
    for i in range(nbit):
        for j in range(nbit):
            homo += glcm[i, j] / (1. + (i - j) ** 2)
    return homo


@njit
def fast_glcm_energy(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm asm, energy
    """
    _, nbit, h, w = glcm.shape
    asm = np.zeros((h, w), dtype=np.float32)
    for i in range(nbit):
        for j in range(nbit):
            asm  += glcm[i, j] ** 2
    return np.sqrt(asm)


def fast_glcm_max(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm max
    """
    return np.max(glcm, axis=(0, 1))


def fast_glcm_entropy(glcm: np.ndarray) -> np.ndarray:
    """
    Calc glcm entropy
    """
    pnorm = glcm / np.sum(glcm, axis=(0, 1)) + 1. / 25
    return np.sum(-pnorm * np.log(pnorm), axis=(0, 1))


def extract_features(image: np.ndarray) -> np.ndarray:
    if image.ndim > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    glcm = fast_glcm(image)

    mean = fast_glcm_mean(glcm)
    std = fast_glcm_std(glcm)
    cont = fast_glcm_contrast(glcm)
    diss = fast_glcm_dissimilarity(glcm)
    homo = fast_glcm_homogeneity(glcm)
    ene = fast_glcm_energy(glcm)
    ma = fast_glcm_max(glcm)
    ent = fast_glcm_entropy(glcm)

    return np.dstack((mean, std, cont, diss, homo, ene, ma, ent))
