"""
Registra en fase3_registro/ los documentos utiles (lista_blanca.csv) que la
cola de Fase 3 nunca proceso, por haberse generado antes de que Fase 1 terminara.
Reutiliza la MISMA logica de id que fase3_cola.py, para que si la cola se
regenera mas adelante, los ids coincidan y no se dupliquen.
"""
import hashlib
import json
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
CARPETA_REGISTRO = RAIZ / "fase3_registro"
CARPETA_REGISTRO.mkdir(exist_ok=True)


def identificador(comuna: str, ruta: str) -> str:
    resumen = hashlib.sha1(ruta.encode("utf-8")).hexdigest()[:10]
    return f"{comuna}_{resumen}".lower()


def ahora() -> str:
    return datetime.now().isoformat(timespec="seconds")


# (comuna, ruta_relativa, paginas, veredicto, resultado)
CASOS = [
    (
        "arauco",
        r"Ordenanzas ordenadas\OCR ok\arauco_110_deja_sin_efecto_declaratorias_de_utilidad_publica_en_relacion_al_plan_regula__resolucion110modificaplanregulador.pdf",
        4, "TEXTO",
        {"tiene_tablas": True, "rangos": [[3, 4]], "confianza": "ALTA", "metodo": "TEXTO",
         "nota": "Trampa 'deja sin efecto' correctamente identificada por Fase 1: el mismo acto tambien promulga la modificacion (area urbana Horcones). p3: usos permitidos/prohibidos por zona (ZH-1,ZH-2,ZE-3,ZE-4,ZI-1,ZI-2,ZPC,ZNE). p4: tabla completa de normas urbanisticas (art.19) con COS, CC, altura, sistema de agrupamiento, superficie predial minima, adosamiento. Documento es 1 pagina de una edicion completa del Diario Oficial (contiene tambien una noticia de partido politico intercalada)."}
    ),
    (
        "coelemu",
        r"Ordenanzas ordenadas\OCR ok\coelemu_189_deja_sin_efecto_resolucion_n_151_de_fecha_31072013_de_intendente_regional_re__do-20160121.pdf",
        44, "TEXTO",
        {"tiene_tablas": True, "rangos": [[4, 4]], "confianza": "ALTA", "metodo": "TEXTO",
         "nota": "Trampa 'deja sin efecto' correctamente identificada por Fase 1. Modificacion puntual: reemplaza la fila Densidad Habitacional Maxima Bruta del Cuadro de Normas Urbanisticas de la Zona S2A Residencial (art.35) por 560 hab/ha. Es un cambio de una sola celda, no una tabla completa nueva. Documento es edicion completa del Diario Oficial (44 pag, mezcla otros avisos ajenos al PRC)."}
    ),
    (
        "huechuraba",
        r"Ordenanzas ordenadas\huechuraba_2450_promulga_aprobacion_de_modificacion_n_4_al_plan_regulador_decreto_exento_n___11.pdf",
        1, "VACIO",
        {"tiene_tablas": False, "rangos": [], "confianza": "ALTA", "metodo": "VISUAL",
         "nota": "Verificado por render (veredicto VACIO era correcto: 0 chars de texto). El documento SOLO reclasifica 3 tramos de vialidad (Av. del Condor, Av. del Valle, Av. Los Jardines) de 'Via de Servicio Existente' a 'Via Colectora' en la columna de observaciones del Cuadro N3 Vialidad Estructurante Comunal (art.72 Ordenanza Local). No modifica coeficientes, usos ni ninguna norma urbanistica de zona. Confirma que sirve=SI de Fase 1 es correcto (es una modificacion real del PRC) pero no aporta tabla de normas."}
    ),
    (
        "molina",
        r"Ordenanzas ordenadas\OCR ok\molina_52_promulga_plan_regulador_comunal_de_molina_y_deja_sin_efecto_resoluciones_afec__Publicacion-del-Miercoles-7-de-Diciembre-de-2022-DIARIO-OFICIAL.pdf",
        30, "TEXTO",
        {"tiene_tablas": True, "rangos": [[15, 21]], "confianza": "ALTA", "metodo": "VISUAL",
         "nota": "TRAMPA NUEVA (no es la trampa LeyChile/Caldera): el veredicto de pagina es TEXTO en promedio, pero las tablas de normas por zona estan insertadas como IMAGEN dentro de un PDF nativo del Diario Oficial digital (2022); el texto solo extrae encabezados de zona (ZU-1, ZU-2...), no los valores. Verificado por render: p15 Art.4.2 lista de zonas (ZU-1 a ZU-7, ZE-1 a ZE-6, ZAP, ZAV) + p16-21 tablas completas por zona (usos de suelo, COS, CC, altura, agrupamiento, antejardin, densidad) terminando en ZAV/ZPL/ICH patrimonial. p22 ya es Titulo 5 Vialidad (fuera de rango). Revisar TODOS los PDFs de Diario Oficial digital 2020+ con este patron -- el veredicto TEXTO no garantiza que las tablas sean texto."}
    ),
    (
        "pedro_aguirre_cerda",
        r"Ordenanzas Descargadas\600-1200\pedro_aguirre_cerda_solicito_informacion_sobre_las_enmiendas_del_plan_regulador_de_la_poblacion_la_v__90bf18e2-3aa9-40c6-96cf-50a519d11220.pdf",
        1, "TEXTO",
        {"tiene_tablas": True, "rangos": [[1, 1]], "confianza": "MEDIA", "metodo": "TEXTO",
         "nota": "Confianza MEDIA porque se acepta la verificacion textual ya hecha por Fase 1 (motivo del CSV), no se rerenderizo aqui. Es una respuesta de Transparencia municipal que, excepcionalmente, SI transcribe contenido normativo real: describe la enmienda que reduce en 30% el coeficiente de constructibilidad y fija coeficiente maximo 0.84 para la zona PAC-1. Excepcion deliberada a la regla general de que 'solicitudes ciudadanas' son tramite."}
    ),
    (
        "penalolen",
        r"Ordenanzas ordenadas\OCR ok\penalolen_Zona_EQ-3.pdf",
        1, "VACIO",
        {"tiene_tablas": True, "rangos": [[1, 1]], "confianza": "MEDIA", "metodo": "TEXTO",
         "nota": "Confianza MEDIA: se acepta verificacion textual ya hecha por Fase 1 (veredicto de pagina decia VACIO pero Fase 1 extrajo texto real con pdftotext directo -- posible inconsistencia del extractor automatico de Fase 0 con este archivo especifico, quizas por tener 3 copias con distinta calidad). Contenido: Zona EQ-3, equipamiento comunitario, vivienda permitida hasta 30% de la superficie del predio."}
    ),
    (
        "romeral",
        r"Ordenanzas ordenadas\OCR ok\romeral_44_promulga_plan_regulador_comunal_de_romeral_y_deja_sin_efecto_resoluciones_que__07306_PRC_ROMERAL_OR_44_17.pdf",
        25, "TEXTO",
        {"tiene_tablas": True, "rangos": [[14, 18]], "confianza": "ALTA", "metodo": "VISUAL",
         "nota": "Misma trampa nueva que Molina: veredicto TEXTO pero tablas de zona en imagen (Diario Oficial digital 2017). Verificado por render: p14 Art.4.2 lista de zonas (ZU-1 a ZU-7, ZAV, ZE-1 a ZE-4) + tabla ZU-1 y ZU-2 completas en la misma pagina; p15-18 resto de zonas. p19 ya es Titulo 5 Vialidad Estructurante (fuera de rango)."}
    ),
    (
        "san_clemente",
        r"Ordenanzas ordenadas\OCR ok\san_clemente_15_promulga_plan_regulador_comunal_de_san_clemente_y_deja_sin_efecto_resolucione__Exportar.pdf",
        28, "MIXTO",
        {"tiene_tablas": True, "rangos": [[16, 22]], "confianza": "ALTA", "metodo": "VISUAL",
         "nota": "Trampa LeyChile clasica (delator 'cuadros siguientes:' + punto solitario) confirmada en p7 y p23. p8-15 son tablas de limite urbano (coordenadas, NO normas). p16: lista de zonas (ZCV, ZU-1 a ZU-8, ZE-1 a ZE-3, ZAV, ZAP, ZNE). p17-22: tablas completas por zona (usos, COS, CC, altura, antejardin, distanciamiento, cierros) terminando en ZAV/ZAP/ZNE. p23 ya es Titulo 3 Vialidad Urbana Local (fuera de rango). Comuna tiene 2 areas urbanas (San Clemente + Aurora Flor del Llano) -- verificar si Aurora Flor del Llano tiene su propio cuadro de zonas separado no capturado en este rango."}
    ),
    (
        "santa_maria",
        r"Ordenanzas Descargadas\1200 x\santa_maria_atribuciones_esenciales__PLANO REGULADOR COMUNAL 01.12.1982.pdf",
        1, "ESCANEADO",
        {"tiene_tablas": True, "rangos": [[1, 1]], "confianza": "MEDIA", "metodo": "VISUAL",
         "nota": "Confianza MEDIA: se acepta verificacion visual ya hecha por Fase 1 (motivo del CSV), no se rerenderizo aqui. Nombre de archivo enganoso ('atribuciones_esenciales', patron generico del portal de transparencia) pero el contenido real es el plano + ordenanza del PRC de Santa Maria (1982): cuadro normativo completo (usos de suelo, superficie predial minima, frente predial minimo, antejardin, rasantes) para zonas H-1, H-2, EC y ZR, con firma de aprobacion SEREMI MINVU. Confirma que Fase 1 correctamente ignoro el nombre y evaluo el contenido."}
    ),
    (
        "teno",
        r"Ordenanzas ordenadas\OCR ok\teno_52_promulga_plan_regulador_comunal_de_teno_y_deja_sin_efecto_resolucion_que_indi__Exportar.pdf",
        34, "MIXTO",
        {"tiene_tablas": True, "rangos": [[15, 23]], "confianza": "ALTA", "metodo": "VISUAL",
         "nota": "Misma trampa LeyChile que San Clemente (delator confirmado en p8, p15, p24, p28). p9-14 son tablas de limite urbano (coordenadas, NO normas), NO incluidas. p15: Capitulo 4 'Zonificacion y Normas Urbanisticas', Art.7, lista de zonas. p16-22: tablas completas por zona (ZU-3, ZU-4 verificadas por render: usos de suelo, superficie predial minima, altura, densidad bruta, agrupamiento, COS, CC). p23: Art.9-10 areas de riesgo y fajas de proteccion (aun dentro del capitulo normativo general, se incluye por criterio de rango generoso). p24 ya es vialidad estructurante (fuera de rango)."}
    ),
]


def main():
    for comuna, ruta, paginas, veredicto, resultado in CASOS:
        id_doc = identificador(comuna, ruta)
        registro = {
            "id": id_doc,
            "comuna": comuna,
            "ruta": ruta,
            "nombre": Path(ruta).name,
            "veredicto": veredicto,
            "paginas": paginas,
            "estado": "HECHO",
            "sesion": "revision-cobertura",
            "inicio": ahora(),
            "fin": ahora(),
            "resultado": {**resultado, "paginas_utiles": sum(b - a + 1 for a, b in resultado["rangos"])},
        }
        ruta_salida = CARPETA_REGISTRO / f"{id_doc}.json"
        if ruta_salida.exists():
            print(f"YA EXISTE, se omite: {id_doc}")
            continue
        ruta_salida.write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"registrado: {id_doc} ({comuna})")


if __name__ == "__main__":
    main()
