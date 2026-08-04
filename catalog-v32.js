(() => {
  const WHATSAPP = '573008507813';
  const entries = {
    'service-diagnostic': {
      type: 'Servicio profesional', code: 'DIAGNOSTIC', title: 'Diagnóstico Jurídico Empresarial',
      summary: 'Evaluación transversal y priorizada para identificar exposiciones jurídicas, decisiones aplazadas y medidas de regularización que pueden afectar continuidad, patrimonio, contratación o crecimiento.',
      duration: '2 a 4 semanas', modality: 'Diagnóstico dirigido', audience: 'Gerencia, socios y dirección administrativa',
      question: '¿Qué exposiciones pueden afectar la continuidad, el patrimonio, la capacidad de contratar o la posibilidad de crecer, y qué debe atenderse primero?',
      situations: [
        ['Crecimiento sin estructura equivalente', 'La operación avanzó más rápido que los contratos, las atribuciones, los registros o los mecanismos de control.'],
        ['Información jurídica dispersa', 'No existe un inventario confiable de contratos, obligaciones, permisos, activos o contingencias.'],
        ['Decisión relevante próxima', 'La empresa prepara inversión, alianza, financiación, expansión, reorganización o contratación material.'],
        ['Exposición acumulada', 'Existen pendientes societarios, contractuales, laborales, regulatorios, de datos o de propiedad intelectual.'],
      ],
      scope: [
        ['Estructura y gobierno', 'Existencia, representación, atribuciones, estatutos, libros, decisiones y formalizaciones materiales.'],
        ['Contratos y relaciones', 'Contratos relevantes, renovaciones, garantías, incumplimientos, dependencia y mecanismos de salida.'],
        ['Activos y cumplimiento', 'Propiedad intelectual, datos, consumidor, relaciones de trabajo, políticas y evidencias.'],
        ['Regulación y operación', 'Permisos, registros, autoridades, obligaciones periódicas y dependencias sectoriales.'],
      ],
      method: [
        ['Comprender', 'Entrevista de dirección, objetivos, decisiones y perímetro.'],
        ['Inventariar', 'Solicitud estructurada de información y responsables.'],
        ['Calificar', 'Revisión de hechos, régimen, evidencia e impacto.'],
        ['Priorizar', 'Riesgos, urgencia, tratamiento, dependencias y responsables.'],
        ['Cerrar', 'Informe ejecutivo, comité de resultados y plan de 90 días.'],
      ],
      deliverables: [
        ['Informe jurídico ejecutivo', 'Conclusiones, supuestos, hallazgos materiales y condiciones que pueden modificar el análisis.'],
        ['Matriz priorizada de riesgos', 'Impacto, probabilidad, urgencia, control existente, tratamiento y riesgo residual.'],
        ['Plan jurídico de 90 días', 'Medidas, responsables, dependencias, evidencias, fechas y criterios de cierre.'],
        ['Comité ejecutivo', 'Presentación de resultados y decisiones que requieren validación de la dirección.'],
      ],
      requirements: [
        ['Patrocinador interno', 'Una persona con autoridad para coordinar información, responsables y decisiones.'],
        ['Perímetro acordado', 'Empresas, operaciones, contratos, proyectos y periodos que harán parte de la revisión.'],
        ['Información mínima', 'Documentos relevantes, listado de pendientes, actores y decisiones próximas.'],
        ['Disponibilidad', 'Entrevistas breves con responsables de áreas críticas cuando corresponda.'],
      ],
      limits: ['No constituye auditoría de aseguramiento absoluto ni certificación integral de cumplimiento.', 'Las conclusiones dependen de la información revelada y del perímetro acordado.', 'Litigios, tributación, seguridad técnica, valoración y auditorías especializadas requieren alcance separado.', 'La implementación de medidas correctivas no está incluida salvo pacto expreso.'],
      related: [
        ['Producto', 'Diagnóstico Jurídico Empresarial', 'Paquete de alcance cerrado para una revisión estandarizada.', '../productos/diagnostico-juridico-empresarial.html'],
        ['Producto', 'Empresa Jurídicamente Organizada', 'Implementación estructurada de prioridades corporativas y operativas.', '../productos/empresa-juridicamente-organizada.html'],
        ['Plan', 'Dirección Jurídica Externa', 'Continuidad para ejecutar, priorizar y actualizar el mapa jurídico.', '../index.html#planes'],
      ],
    },
    'service-direction': {
      type: 'Servicio profesional', code: 'LEGAL_DIRECTION', title: 'Dirección Jurídica Externa',
      summary: 'Capacidad jurídica recurrente para integrar decisiones, priorizar solicitudes, coordinar especialistas y conservar memoria institucional sin convertir la relación en disponibilidad ilimitada.',
      duration: 'Mensual o trimestral', modality: 'Plan recurrente', audience: 'Gerencia y empresas sin dirección jurídica interna completa',
      question: '¿Quién integra jurídicamente las decisiones, administra la demanda y asegura que las recomendaciones se conviertan en acciones, responsables y evidencia?',
      situations: [
        ['Demanda jurídica fragmentada', 'Las solicitudes llegan por canales informales y se atienden sin prioridades, responsables o seguimiento.'],
        ['Gerencia sin contraparte jurídica', 'Las decisiones requieren criterio permanente, pero no justifican todavía una dirección interna completa.'],
        ['Varios proveedores externos', 'La empresa necesita coordinar especialistas y conservar una posición jurídica común.'],
        ['Pérdida de memoria', 'Contratos, conceptos y decisiones dependen de personas o correos y no de un sistema institucional.'],
      ],
      scope: [
        ['Gobierno del servicio', 'Comité, agenda, prioridades, reglas de escalamiento y registro de decisiones.'],
        ['Triage preventivo', 'Calificación inicial de solicitudes dentro del volumen y niveles de servicio acordados.'],
        ['Riesgos y obligaciones', 'Seguimiento de contingencias, vencimientos, compromisos y medidas de tratamiento.'],
        ['Coordinación especializada', 'Definición de instrucciones y articulación con litigantes, tributarios, técnicos u otros asesores.'],
      ],
      method: [
        ['Configurar', 'Demanda, usuarios, canales, prioridades, SLA y exclusiones.'],
        ['Recibir', 'Registro y clasificación de solicitudes y decisiones.'],
        ['Resolver', 'Concepto, revisión, negociación o definición de proyecto.'],
        ['Controlar', 'Obligaciones, evidencia, vencimientos y riesgos.'],
        ['Informar', 'Comité e informe ejecutivo con decisiones y carga.'],
      ],
      deliverables: [
        ['Tablero jurídico ejecutivo', 'Solicitudes, riesgos, obligaciones, vencimientos y estado de decisiones.'],
        ['Agenda de dirección', 'Asuntos que requieren criterio, aprobación, inversión o escalamiento.'],
        ['Atención dentro del alcance', 'Conceptos, revisiones y acompañamientos conforme al volumen pactado.'],
        ['Memoria institucional', 'Registro de posiciones, documentos aprobados, responsables y antecedentes.'],
      ],
      requirements: [
        ['Responsable de relación', 'Interlocutor con capacidad para consolidar prioridades y validar decisiones.'],
        ['Canal único', 'Mecanismo definido para ingresar solicitudes y evitar trabajo fuera de trazabilidad.'],
        ['Volumen estimado', 'Tipos de asuntos, frecuencia, usuarios y tiempos esperados.'],
        ['Gobierno interno', 'Aprobadores, responsables comerciales, financieros, técnicos y operativos.'],
      ],
      limits: ['No implica disponibilidad ilimitada ni respuesta inmediata para cualquier asunto.', 'Representación judicial, transacciones extraordinarias y proyectos especiales se cotizan por separado.', 'La capacidad mensual, los tiempos, las revisiones y los canales deben pactarse expresamente.', 'Las decisiones comerciales y operativas permanecen en cabeza de la empresa.'],
      related: [
        ['Servicio', 'Legal Operations', 'Diseño del modelo operativo que soporta la relación jurídica.', 'legal-operations.html'],
        ['Producto', 'Sistema Contractual Empresarial', 'Estandarización de contratación, playbooks y obligaciones.', '../productos/sistema-contractual-empresarial.html'],
        ['Demostración', 'Meridiano Empresas', 'Vista de solicitudes, expedientes, obligaciones y riesgos.', '../demo.html'],
      ],
    },
    'service-contracts': {
      type: 'Servicio profesional', code: 'CONTRACTS', title: 'Contratación Estratégica y Gestión Contractual',
      summary: 'Estructuración, revisión y negociación de contratos para traducir el acuerdo comercial, distribuir riesgos y preservar opciones razonables durante ejecución, cambio, incumplimiento y terminación.',
      duration: 'Según negociación o proyecto', modality: 'Servicio o proyecto', audience: 'Comercial, compras, gerencia y operación',
      question: '¿El contrato refleja realmente la operación, asigna los riesgos a quien puede controlarlos y puede administrarse después de la firma?',
      situations: [
        ['Negociación material', 'La empresa enfrenta posiciones relevantes sobre precio, responsabilidad, propiedad intelectual, garantías o salida.'],
        ['Modelos que no reflejan la operación', 'Los contratos se reutilizan sin adaptar objeto, hitos, aceptación, cambios o dependencias.'],
        ['Incumplimiento o renegociación', 'Debe preservarse evidencia, exigir cumplimiento, gestionar cambios o preparar una terminación.'],
        ['Alto volumen contractual', 'La organización necesita criterios, playbooks y obligaciones administrables.'],
      ],
      scope: [
        ['Formación y autoridad', 'Etapa precontractual, ofertas, aprobaciones, facultades y formación del consentimiento.'],
        ['Arquitectura económica y operativa', 'Objeto, alcance, precio, hitos, aceptación, cambios, pagos y dependencias.'],
        ['Asignación de riesgos', 'Garantías, indemnidad, responsabilidad, seguros, fuerza mayor y límites.'],
        ['Activos, datos y salida', 'Propiedad intelectual, confidencialidad, datos, cumplimiento, suspensión y terminación.'],
      ],
      method: [
        ['Entender', 'Resultado comercial, operación, posiciones y restricciones.'],
        ['Mapear', 'Riesgos, dependencias, aprobadores y puntos de negociación.'],
        ['Estructurar', 'Documento, comentarios o matriz de posiciones.'],
        ['Negociar', 'Soporte en intercambios, alternativas y cierres.'],
        ['Transferir', 'Obligaciones, responsables, evidencias y preavisos.'],
      ],
      deliverables: [
        ['Contrato o control de cambios', 'Documento coherente con las posiciones aprobadas y el modelo operativo.'],
        ['Matriz ejecutiva de posiciones', 'Punto, riesgo, posición propia, contraparte, alternativa y aprobador.'],
        ['Soporte de negociación', 'Preparación de argumentos, alternativas, minutas y registro de acuerdos.'],
        ['Ficha de administración', 'Obligaciones, hitos, evidencias, garantías, renovaciones y terminación.'],
      ],
      requirements: [
        ['Responsable comercial', 'Persona que defina el resultado económico y las concesiones posibles.'],
        ['Descripción operativa', 'Flujo real del servicio, suministro, tecnología, proyecto o relación.'],
        ['Documentos de negociación', 'Borradores, anexos, propuestas, comunicaciones y acuerdos previos.'],
        ['Autoridad definida', 'Aprobadores de responsabilidad, precio, garantías, datos y propiedad intelectual.'],
      ],
      limits: ['No sustituye validaciones técnicas, financieras, tributarias, contables o de seguros.', 'La empresa debe definir posiciones comerciales y autoridad para negociar.', 'No se garantiza aceptación de la contraparte ni cierre de la transacción.', 'La administración posterior requiere responsables internos o un servicio recurrente.'],
      related: [
        ['Producto', 'Sistema Contractual Empresarial', 'Playbook, modelos aprobados, flujo y registro de obligaciones.', '../productos/sistema-contractual-empresarial.html'],
        ['Documento', 'Contrato de prestación de servicios', 'Documento guiado para relaciones delimitadas.', '../demo.html#documentos'],
        ['Plan', 'Gestión Contractual Continua', 'Capacidad recurrente para revisión, negociación y seguimiento.', '../index.html#planes'],
      ],
    },
    'service-corporate': {
      type: 'Servicio profesional', code: 'CORPORATE', title: 'Sociedades, Gobierno e Inversión',
      summary: 'Diseño y formalización de reglas sobre capital, control, órganos, atribuciones, inversión, permanencia y salida para que la estructura societaria corresponda al negocio y a sus riesgos.',
      duration: 'Según operación societaria', modality: 'Proyecto societario', audience: 'Socios, fundadores, juntas e inversionistas',
      question: '¿Las reglas reflejan quién aporta, quién decide, cómo se controla la empresa y qué ocurre ante conflicto, incumplimiento, inversión o salida?',
      situations: [
        ['Acuerdos informales entre socios', 'Las reglas económicas y políticas existen en conversaciones, pero no en instrumentos exigibles.'],
        ['Entrada de inversión', 'La empresa debe preparar capital, autorizaciones, información, derechos y condiciones de cierre.'],
        ['Crecimiento y delegación', 'La representación y las atribuciones no corresponden a la escala actual.'],
        ['Conflicto o transición', 'Se requiere ordenar votaciones, bloqueos, transferencias, permanencia o salida.'],
      ],
      scope: [
        ['Capital y derechos', 'Clases, aportes, dilución, derechos económicos, políticos y mecanismos de ajuste.'],
        ['Órganos y atribuciones', 'Asamblea, junta, representación, comités, mayorías, vetos y materias reservadas.'],
        ['Relación entre socios', 'Permanencia, transferencia, preferencia, acompañamiento, arrastre, salida y bloqueos.'],
        ['Formalización', 'Actas, estatutos, acuerdos, libros, registros, poderes y obligaciones posteriores.'],
      ],
      method: [
        ['Diagnosticar', 'Estructura actual, cap table, decisiones y riesgos.'],
        ['Diseñar', 'Principios económicos, políticos y de control.'],
        ['Negociar', 'Posiciones, alternativas y materias reservadas.'],
        ['Documentar', 'Estatutos, acuerdos, actas o instrumentos de inversión.'],
        ['Formalizar', 'Firmas, registros, libros, poderes y calendario.'],
      ],
      deliverables: [
        ['Arquitectura societaria', 'Mapa de capital, órganos, atribuciones, aprobaciones y dependencias.'],
        ['Instrumentos societarios', 'Estatutos, acuerdos de accionistas, actas, reglamentos o poderes.'],
        ['Matriz de materias reservadas', 'Decisiones, órgano competente, mayoría, veto y evidencia.'],
        ['Plan de formalización', 'Secuencia, responsables, documentos, registros y condiciones de eficacia.'],
      ],
      requirements: [
        ['Cap table y documentos vigentes', 'Certificados, estatutos, acuerdos, actas y libros disponibles.'],
        ['Objetivo económico', 'Inversión, reorganización, gobierno, permanencia, salida o solución del conflicto.'],
        ['Posiciones de los socios', 'Derechos, restricciones, aportes, control y expectativas.'],
        ['Información de la transacción', 'Términos, valoración, condiciones, cronograma y asesores relacionados.'],
      ],
      limits: ['Valoración, tributación, contabilidad y asesoría de inversión requieren especialistas.', 'La eficacia depende de aprobaciones, firmas, registros y actualización de libros.', 'No se garantiza consenso entre socios ni cierre de inversión.', 'Controversias judiciales o arbitrales requieren representación separada.'],
      related: [
        ['Producto', 'Empresa Lista para Inversión', 'Preparación jurídica, gobierno, activos y data room.', '../productos/empresa-lista-para-inversion.html'],
        ['Producto', 'Empresa Jurídicamente Organizada', 'Regularización de estructura, atribuciones y documentación.', '../productos/empresa-juridicamente-organizada.html'],
        ['Plan', 'Secretaría Societaria', 'Continuidad para órganos, actas, libros y decisiones.', '../index.html#planes'],
      ],
    },
    'service-ip': {
      type: 'Servicio profesional', code: 'IP', title: 'Propiedad Intelectual y Activos Intangibles',
      summary: 'Estrategia jurídica para identificar, probar, proteger y explotar marcas, software, contenidos, secretos empresariales y demás activos que concentran valor y diferenciación.',
      duration: 'Según activo o portafolio', modality: 'Proyecto por activo', audience: 'Empresas tecnológicas, marcas, creadores y equipos de innovación',
      question: '¿La empresa puede demostrar quién creó sus activos, quién es titular y bajo qué condiciones puede usarlos, licenciarlos, transferirlos o defenderlos?',
      situations: [
        ['Software desarrollado por terceros', 'No existe una cadena clara de creación, cesión, licencia y componentes.'],
        ['Marca en expansión', 'La empresa necesita definir titular, clases, territorio, uso y vigilancia.'],
        ['Conocimiento crítico expuesto', 'La información reservada no tiene controles contractuales y operativos suficientes.'],
        ['Inversión o transacción', 'Debe probarse titularidad, libertad de uso y ausencia de dependencias ocultas.'],
      ],
      scope: [
        ['Inventario y titularidad', 'Autores, creadores, contratos, cesiones, licencias, registros y evidencias.'],
        ['Protección registral', 'Marcas, clases, titulares, búsquedas, solicitudes, renovaciones y vigilancia.'],
        ['Explotación contractual', 'Licencias, cesiones, distribución, desarrollo, soporte, territorio y remuneración.'],
        ['Reserva y componentes', 'Secretos, accesos, medidas razonables, software de terceros y licencias abiertas.'],
      ],
      method: [
        ['Inventariar', 'Activos, autores, usos, mercados y documentación.'],
        ['Probar', 'Cadena de titularidad, contratos y evidencias.'],
        ['Priorizar', 'Valor, exposición, urgencia y alternativas de protección.'],
        ['Instrumentar', 'Solicitudes, cesiones, licencias y medidas de reserva.'],
        ['Vigilar', 'Renovaciones, usos, terceros, dependencias y actualizaciones.'],
      ],
      deliverables: [
        ['Inventario jurídico', 'Activo, creador, titular, evidencia, uso, territorio y estado de protección.'],
        ['Cadena de titularidad', 'Brechas, documentos faltantes y plan de regularización.'],
        ['Estrategia de protección', 'Mecanismo, jurisdicción, prioridad, costo externo y cronograma.'],
        ['Instrumentos prioritarios', 'Cesiones, licencias, cláusulas, acuerdos de confidencialidad o protocolos.'],
      ],
      requirements: [
        ['Descripción de activos', 'Nombre, función, creador, fecha, uso, mercado y valor estratégico.'],
        ['Contratos históricos', 'Desarrollo, empleo, servicios, licencias, adquisición y colaboración.'],
        ['Material probatorio', 'Repositorios, versiones, facturas, correos, registros y evidencias de uso.'],
        ['Estrategia comercial', 'Productos, territorios, canales, socios y formas de explotación previstas.'],
      ],
      limits: ['No garantiza concesión registral, ausencia de oposición o disponibilidad absoluta.', 'Patentes, litigios y estrategias multijurisdiccionales pueden exigir especialistas.', 'La protección de secretos depende de medidas técnicas, humanas y operativas adicionales.', 'La libertad de operación técnica no se presume a partir de una revisión contractual.'],
      related: [
        ['Producto', 'Marca, Software y Activos Intangibles Protegidos', 'Regularización y protección de un portafolio delimitado.', '../productos/activos-intangibles-protegidos.html'],
        ['Servicio', 'Tecnología e inteligencia artificial', 'Contratos, datos, proveedores y gobernanza tecnológica.', 'tecnologia-inteligencia-artificial.html'],
        ['Documento', 'Cesión o licencia de software', 'Documento guiado para casos delimitados.', '../demo.html#documentos'],
      ],
    },
    'service-ai': {
      type: 'Servicio profesional', code: 'AI_GOVERNANCE', title: 'Tecnología e Inteligencia Artificial',
      summary: 'Gobernanza jurídica de sistemas, proveedores, datos y casos de uso para adoptar tecnología e inteligencia artificial con responsabilidades, controles, supervisión y evidencia proporcionales al impacto.',
      duration: 'Proyecto o programa', modality: 'Diagnóstico e implementación', audience: 'Dirección, tecnología, datos, innovación y cumplimiento',
      question: '¿La organización sabe dónde usa inteligencia artificial, qué datos intervienen, quién responde, cómo supervisa resultados y qué debe hacer ante un incidente?',
      situations: [
        ['Adopción dispersa de herramientas', 'Las áreas contratan o usan IA sin inventario, aprobación, reglas de datos o supervisión.'],
        ['Desarrollo de soluciones propias', 'Debe definirse responsabilidad, entrenamiento, pruebas, usuarios, terceros y límites de uso.'],
        ['Proveedor tecnológico crítico', 'El contrato no ofrece suficiente trazabilidad, control, continuidad o gestión de incidentes.'],
        ['Decisiones sobre personas', 'La tecnología influye en empleo, clientes, crédito, salud, acceso o evaluación.'],
      ],
      scope: [
        ['Inventario de sistemas', 'Casos de uso, propietarios, proveedores, datos, usuarios y grupos afectados.'],
        ['Clasificación de riesgo', 'Impacto, autonomía, reversibilidad, sensibilidad, escala y supervisión.'],
        ['Gobierno y contratación', 'Aprobaciones, roles, debida diligencia, garantías, auditoría, datos y salida.'],
        ['Controles e incidentes', 'Supervisión humana, transparencia, pruebas, registro, capacitación y respuesta.'],
      ],
      method: [
        ['Descubrir', 'Casos, sistemas, datos, proveedores y decisiones.'],
        ['Clasificar', 'Riesgo jurídico, impacto y nivel de control requerido.'],
        ['Diseñar', 'Política, roles, aprobaciones y debida diligencia.'],
        ['Implementar', 'Contratos, registros, controles, capacitación e incidentes.'],
        ['Revisar', 'Cambios, desempeño, incidentes y riesgo residual.'],
      ],
      deliverables: [
        ['Inventario de IA', 'Caso, finalidad, responsable, proveedor, datos, usuarios y estado.'],
        ['Matriz de clasificación', 'Criterios de riesgo, controles, aprobación y revisión requerida.'],
        ['Marco de gobernanza', 'Política, roles, comité, procedimiento de aprobación y excepciones.'],
        ['Kit de control', 'Checklist de proveedor, cláusulas, registro de incidentes y plan de capacitación.'],
      ],
      requirements: [
        ['Patrocinio interdisciplinario', 'Dirección, tecnología, datos, seguridad, talento y operación.'],
        ['Inventario inicial', 'Herramientas conocidas, proveedores, pilotos y desarrollos propios.'],
        ['Información técnica disponible', 'Arquitectura, fuentes de datos, integraciones, pruebas y controles.'],
        ['Casos prioritarios', 'Usos con mayor impacto, escala, sensibilidad o exposición contractual.'],
      ],
      limits: ['No constituye auditoría técnica, certificación algorítmica, pentesting ni evaluación científica del modelo.', 'Casos de alto impacto pueden requerir especialistas técnicos, éticos, sectoriales y de seguridad.', 'No se garantiza ausencia de sesgos, errores o incidentes.', 'La gobernanza exige actualización continua y no se agota en una política.'],
      related: [
        ['Producto', 'Programa de Gobernanza de IA', 'Implementación estructurada de inventario, política y controles.', '../productos/programa-gobernanza-ia.html'],
        ['Servicio', 'Propiedad Intelectual', 'Titularidad, licencias, datasets y activos tecnológicos.', 'propiedad-intelectual.html'],
        ['Servicio', 'Legal Operations', 'Procesos y tecnología para administrar aprobaciones y evidencia.', 'legal-operations.html'],
      ],
    },
    'service-regulated': {
      type: 'Servicio profesional', code: 'REGULATED', title: 'Estructuración Jurídica de Proyectos Regulados',
      summary: 'Análisis de viabilidad y arquitectura jurídica para proyectos cuya ejecución depende de autoridades, permisos, habilitaciones, actores públicos o privados, regulación sectorial y secuencias críticas.',
      duration: '3 a 12 semanas', modality: 'Proyecto de viabilidad', audience: 'Promotores, inversionistas, municipios, operadores y aliados',
      question: '¿El proyecto debe avanzar, rediseñarse o detenerse antes de comprometer recursos, firmar contratos o iniciar operación?',
      situations: [
        ['Modelo nuevo o híbrido', 'La actividad no encaja de manera inmediata en una categoría regulatoria conocida.'],
        ['Múltiples autoridades', 'La viabilidad depende de competencias, permisos y decisiones con secuencia específica.'],
        ['Alianza público-privada', 'Deben definirse roles, aportes, riesgos, contraprestaciones y mecanismos de control.'],
        ['Inversión previa a permisos', 'Se necesita ordenar condiciones precedentes antes de comprometer capital.'],
      ],
      scope: [
        ['Actividad y régimen', 'Descripción funcional, territorio, usuarios, bienes, servicios y normativa aplicable.'],
        ['Autoridades y permisos', 'Competencias, habilitaciones, registros, secuencia, vigencias y dependencias.'],
        ['Actores y responsabilidades', 'Promotor, operador, propietario, financiador, municipio, proveedor y usuario.'],
        ['Arquitectura contractual', 'Vehículo, alianzas, condiciones precedentes, garantías, remuneración y control.'],
      ],
      method: [
        ['Modelar', 'Actividad, territorio, flujo económico y operación.'],
        ['Calificar', 'Regímenes, autoridades, permisos y restricciones.'],
        ['Mapear', 'Actores, funciones, riesgos y dependencias.'],
        ['Estructurar', 'Vehículo, contratos, condiciones y hoja de ruta.'],
        ['Validar', 'Supuestos técnicos, financieros y regulatorios críticos.'],
      ],
      deliverables: [
        ['Concepto ejecutivo de viabilidad', 'Conclusión condicionada, supuestos, riesgos y decisiones de avance.'],
        ['Mapa de autoridades y actores', 'Competencia, función, interacción, documento y dependencia.'],
        ['Matriz de permisos y contratos', 'Requisito, responsable, secuencia, evidencia, vigencia y condición precedente.'],
        ['Hoja de ruta jurídica', 'Etapas, hitos, contratos, aprobaciones y puntos de no retorno.'],
      ],
      requirements: [
        ['Descripción técnica', 'Proceso, capacidad, localización, insumos, productos, usuarios y tecnología.'],
        ['Modelo económico', 'Ingresos, pagos, aportes, activos, costos y relaciones principales.'],
        ['Mapa preliminar de actores', 'Autoridades, propietarios, operadores, financiadores y aliados.'],
        ['Estudios disponibles', 'Técnicos, ambientales, sanitarios, tarifarios, financieros o territoriales.'],
      ],
      limits: ['No sustituye estudios técnicos, ambientales, sanitarios, tarifarios, financieros o de ingeniería.', 'No garantiza permisos, financiación, adjudicación ni decisiones de terceros.', 'Trámites, representación y negociación contractual se dimensionan por separado.', 'Cambios regulatorios o técnicos pueden modificar la conclusión.'],
      related: [
        ['Producto', 'Proyecto Regulado Estructurado', 'Paquete de viabilidad, actores, permisos y hoja de ruta.', '../productos/proyecto-regulado-estructurado.html'],
        ['Plan', 'Gestión Jurídica Regulatoria', 'Seguimiento recurrente de permisos, cambios y obligaciones.', '../index.html#planes'],
        ['Servicio', 'Contratación estratégica', 'Instrumentación de alianzas, operación y condiciones precedentes.', 'contratacion-estrategica.html'],
      ],
    },
    'service-ops': {
      type: 'Servicio profesional', code: 'LEGAL_OPS', title: 'Legal Operations y Transformación de la Función Jurídica',
      summary: 'Diseño del modelo operativo, los flujos, documentos, métricas y herramientas que permiten administrar la demanda jurídica con trazabilidad, capacidad y mejora continua.',
      duration: '6 a 16 semanas', modality: 'Proyecto de transformación', audience: 'Áreas jurídicas, administrativas, compras y gerencia',
      question: '¿La organización puede administrar solicitudes, documentos, obligaciones y decisiones sin depender de canales informales, personas específicas o memoria individual?',
      situations: [
        ['Sobrecarga y falta de prioridades', 'Todos los asuntos parecen urgentes y no existe criterio común de triage.'],
        ['Documentos sin gobierno', 'Existen múltiples versiones, modelos no aprobados y poca trazabilidad de cambios.'],
        ['Solicitudes por correo y mensajería', 'No hay expediente, responsable, estado, SLA ni evidencia de cierre.'],
        ['Tecnología sin proceso', 'Se implementan herramientas sin taxonomía, roles, datos o gestión del cambio.'],
      ],
      scope: [
        ['Demanda y catálogo', 'Usuarios, necesidades, tipos de servicio, volumen, complejidad y canales.'],
        ['Triage y flujos', 'Criterios, etapas, responsables, aprobaciones, escalamiento y cierre.'],
        ['Documentos y conocimiento', 'Plantillas, versiones, permisos, precedentes, cláusulas y actualización.'],
        ['Datos y tecnología', 'Indicadores, expedientes, obligaciones, automatización e integraciones.'],
      ],
      method: [
        ['Diagnosticar', 'Demanda, capacidad, fricción, herramientas y riesgos.'],
        ['Diseñar', 'Catálogo, taxonomía, triage, flujos y RACI.'],
        ['Construir', 'Plantillas, tableros, expedientes y reglas.'],
        ['Implementar', 'Pilotos, capacitación, canales y gobierno.'],
        ['Mejorar', 'Indicadores, retroalimentación y ciclos de ajuste.'],
      ],
      deliverables: [
        ['Modelo operativo', 'Catálogo, demanda, canales, niveles de servicio y reglas de gobierno.'],
        ['Flujos y matriz de roles', 'Etapas, decisiones, responsables, aprobaciones, escalamiento y cierre.'],
        ['Banco documental gobernado', 'Modelos, metadatos, versiones, permisos y calendario de revisión.'],
        ['Tablero de indicadores', 'Volumen, tiempo, carga, estado, riesgo, autoservicio y satisfacción.'],
      ],
      requirements: [
        ['Datos de demanda', 'Solicitudes, contratos, usuarios, tiempos, documentos y canales disponibles.'],
        ['Patrocinio de dirección', 'Autoridad para cambiar procesos, roles, canales y responsabilidades.'],
        ['Equipo de implementación', 'Jurídico, operación, tecnología, seguridad y usuarios clave.'],
        ['Capacidad de cambio', 'Tiempo para pilotos, capacitación, depuración y adopción.'],
      ],
      limits: ['La tecnología no corrige falta de capacidad, prioridades o decisiones indefinidas.', 'Integraciones, migraciones masivas, desarrollo y ciberseguridad requieren alcance técnico.', 'Los resultados dependen de adopción, gobierno y disciplina operativa.', 'No se automatizan decisiones jurídicas que requieran criterio profesional sin controles.'],
      related: [
        ['Producto', 'Sistema Contractual Empresarial', 'Caso de transformación focal sobre contratación.', '../productos/sistema-contractual-empresarial.html'],
        ['Plan', 'Banco Documental y Legal Operations', 'Soporte recurrente para gobierno y mejora.', '../index.html#planes'],
        ['Demostración', 'Meridiano Empresas', 'Solicitudes, expedientes, documentos, obligaciones y analítica.', '../demo.html'],
      ],
    },
    'product-diagnostic': {
      type: 'Producto jurídico', code: 'P01', title: 'Diagnóstico Jurídico Empresarial',
      summary: 'Producto de alcance cerrado para obtener una lectura ejecutiva de la exposición jurídica, una matriz priorizada y un plan de intervención de 90 días.',
      duration: '2 a 4 semanas', modality: 'Precio y alcance por perímetro', audience: 'Empresas que necesitan un punto de partida confiable',
      question: '¿Dónde está hoy la mayor exposición jurídica y qué decisiones no deberían seguir aplazándose?',
      situations: [['Inicio de ordenamiento', 'La empresa necesita una primera fotografía transversal antes de contratar proyectos separados.'], ['Crecimiento o inversión', 'Se requiere identificar brechas antes de presentar información o comprometer recursos.'], ['Cambio de administración', 'La nueva dirección necesita conocer pendientes, riesgos y responsables.'], ['Acumulación de contingencias', 'Existen señales dispersas, pero no una priorización común.']],
      scope: [['Perímetro definido', 'Una sociedad, operación, proyecto o conjunto de relaciones previamente acordado.'], ['Revisión documental focal', 'Documentos materiales y muestras representativas, no revisión exhaustiva de todo archivo.'], ['Entrevistas clave', 'Dirección y responsables de los frentes incluidos.'], ['Priorización ejecutiva', 'Riesgos, decisiones, medidas y dependencias.']],
      method: [['Activar', 'Perímetro, lista de información y responsables.'], ['Revisar', 'Documentos, hechos y entrevistas.'], ['Calificar', 'Riesgo, impacto, urgencia y evidencia.'], ['Priorizar', 'Tratamiento y plan de 90 días.'], ['Cerrar', 'Informe y comité ejecutivo.']],
      deliverables: [['Informe ejecutivo', 'Hallazgos materiales, supuestos y conclusiones.'], ['Matriz de riesgos', 'Priorización, control y tratamiento.'], ['Plan de 90 días', 'Responsables, hitos y evidencia.'], ['Calendario inicial', 'Decisiones, vencimientos y dependencias.']],
      requirements: [['Perímetro', 'Definición de empresa, áreas y periodos.'], ['Documentos mínimos', 'Societarios, contractuales, laborales, activos y permisos relevantes.'], ['Responsable interno', 'Coordinación de información y entrevistas.'], ['Declaración de pendientes', 'Contingencias, reclamos y decisiones próximas.']],
      limits: ['Revisión focal y no auditoría exhaustiva.', 'La profundidad depende del perímetro y la evidencia disponible.', 'La corrección de hallazgos se contrata separadamente.', 'No incluye litigios, tributación ni auditorías técnicas.'],
      related: [['Servicio', 'Diagnóstico Jurídico Empresarial', 'Versión a la medida para perímetros o complejidades especiales.', '../servicios/diagnostico-juridico-empresarial.html'], ['Producto', 'Empresa Jurídicamente Organizada', 'Ejecución de prioridades y regularización.', 'empresa-juridicamente-organizada.html'], ['Plan', 'Dirección Jurídica Externa', 'Seguimiento de la implementación.', '../index.html#planes']],
    },
    'product-organized': {
      type: 'Producto jurídico', code: 'P02', title: 'Empresa Jurídicamente Organizada',
      summary: 'Programa de regularización para ordenar estructura societaria, atribuciones, contratos esenciales, obligaciones, documentos y responsables de una empresa en crecimiento.',
      duration: '6 a 10 semanas', modality: 'Proyecto de implementación', audience: 'Pymes y empresas en expansión',
      question: '¿La empresa puede crecer y contratar sin depender de memoria, improvisación o acuerdos verbales?',
      situations: [['Estructura informal', 'Decisiones, poderes, contratos y políticas no reflejan la operación.'], ['Crecimiento acelerado', 'La empresa incorpora personas, canales, activos o aliados sin actualizar su base jurídica.'], ['Preparación para terceros', 'Bancos, clientes, inversionistas o aliados solicitan orden documental.'], ['Dependencia personal', 'La información y las decisiones están concentradas en pocas personas.']],
      scope: [['Gobierno y atribuciones', 'Representación, órganos, decisiones, poderes y formalizaciones.'], ['Contratos esenciales', 'Clientes, proveedores, trabajadores, servicios, confidencialidad y activos.'], ['Obligaciones y calendario', 'Renovaciones, registros, permisos, políticas y evidencias.'], ['Banco documental', 'Documentos aprobados, versiones, responsables y reglas de uso.']],
      method: [['Diagnosticar', 'Brechas prioritarias y perímetro.'], ['Diseñar', 'Arquitectura mínima viable.'], ['Documentar', 'Instrumentos y matrices.'], ['Formalizar', 'Aprobaciones, firmas, libros y registros.'], ['Transferir', 'Responsables, calendario y guía de mantenimiento.']],
      deliverables: [['Mapa societario y de atribuciones', 'Órganos, responsables y aprobaciones.'], ['Matriz contractual', 'Relaciones, documentos y estado.'], ['Paquete esencial', 'Instrumentos priorizados dentro del alcance.'], ['Calendario jurídico', 'Obligaciones, vencimientos y responsables.']],
      requirements: [['Diagnóstico o inventario', 'Base de hallazgos o levantamiento inicial.'], ['Disponibilidad de socios', 'Definiciones y aprobaciones oportunas.'], ['Información operativa', 'Relaciones, procesos, personas y activos.'], ['Responsables internos', 'Implementación y mantenimiento.']],
      limits: ['No cubre saneamientos históricos complejos ni litigios.', 'Reorganizaciones, insolvencia y tributación se separan.', 'Tasas, notarías y registros no se incluyen salvo indicación.', 'La empresa debe ejecutar decisiones y adoptar los documentos.'],
      related: [['Servicio', 'Sociedades, Gobierno e Inversión', 'Intervención a la medida para estructuras complejas.', '../servicios/sociedades-gobierno-inversion.html'], ['Producto', 'Sistema Contractual Empresarial', 'Profundización sobre contratación.', 'sistema-contractual-empresarial.html'], ['Producto', 'Activos Intangibles Protegidos', 'Regularización de titularidad y explotación.', 'activos-intangibles-protegidos.html']],
    },
    'product-assets': {
      type: 'Producto jurídico', code: 'P03', title: 'Marca, Software y Activos Intangibles Protegidos',
      summary: 'Paquete para inventariar activos, verificar titularidad, cerrar brechas contractuales y definir una estrategia priorizada de protección y explotación.',
      duration: '3 a 8 semanas', modality: 'Proyecto por portafolio', audience: 'Empresas con marcas, software, contenidos o conocimiento crítico',
      question: '¿La empresa controla jurídicamente los activos que está financiando, usando y explotando?',
      situations: [['Desarrollo tercerizado', 'Software, diseños o contenidos fueron creados por proveedores o colaboradores.'], ['Marca no protegida', 'El uso comercial creció sin estrategia registral suficiente.'], ['Inversión o venta', 'Un tercero solicita probar titularidad y libertad de uso.'], ['Secretos sin medidas', 'Información crítica circula sin controles razonables.']],
      scope: [['Inventario', 'Activos, creadores, usos, mercados y evidencias.'], ['Cadena de titularidad', 'Contratos, cesiones, licencias y brechas.'], ['Protección', 'Marcas, reserva, contratos y prioridades.'], ['Explotación', 'Licencias, territorios, canales, terceros y restricciones.']],
      method: [['Inventariar', 'Activos y evidencias.'], ['Verificar', 'Titularidad y dependencias.'], ['Priorizar', 'Valor, riesgo y urgencia.'], ['Regularizar', 'Contratos y solicitudes.'], ['Mantener', 'Calendario y vigilancia.']],
      deliverables: [['Inventario jurídico', 'Activo, titular, evidencia y estado.'], ['Cadena de titularidad', 'Brechas y plan de cierre.'], ['Estrategia de protección', 'Mecanismos y cronograma.'], ['Instrumentos prioritarios', 'Cesiones, licencias o cláusulas.']],
      requirements: [['Listado de activos', 'Marcas, software, contenidos y conocimiento.'], ['Contratos', 'Creación, empleo, servicios y licencias.'], ['Evidencias', 'Repositorios, versiones, facturas y uso.'], ['Mercados', 'Territorios, canales y explotación prevista.']],
      limits: ['No garantiza concesión registral ni ausencia de oposición.', 'Litigios, patentes y búsquedas técnicas se separan.', 'La protección internacional requiere alcance específico.', 'Los costos oficiales y de terceros se informan aparte.'],
      related: [['Servicio', 'Propiedad Intelectual', 'Asesoría a la medida y negociación de activos.', '../servicios/propiedad-intelectual.html'], ['Producto', 'Empresa Lista para Inversión', 'Integración de activos en preparación para transacción.', 'empresa-lista-para-inversion.html'], ['Documento', 'Cesión o licencia de software', 'Documento guiado para casos delimitados.', '../demo.html#documentos']],
    },
    'product-investment': {
      type: 'Producto jurídico', code: 'P04', title: 'Empresa Lista para Inversión',
      summary: 'Preparación jurídica para reducir fricción en una revisión de inversionistas mediante gobierno, cap table, contratos, activos, contingencias y data room organizados.',
      duration: '6 a 12 semanas', modality: 'Proyecto de preparación', audience: 'Startups, pymes y empresas en ronda o transacción',
      question: '¿La estructura jurídica resiste una revisión razonable de inversionistas y permite explicar las contingencias sin improvisación?',
      situations: [['Ronda próxima', 'La empresa prepara acercamientos, term sheet o due diligence.'], ['Cap table inconsistente', 'Aportes, opciones, acuerdos o registros no coinciden.'], ['Activos críticos dispersos', 'La titularidad de software, marca o contratos no está consolidada.'], ['Data room incompleto', 'No existe índice, responsable ni narrativa de contingencias.']],
      scope: [['Gobierno y capital', 'Cap table, estatutos, acuerdos, órganos y aprobaciones.'], ['Contratos materiales', 'Clientes, proveedores, talento, tecnología y obligaciones.'], ['Activos y cumplimiento', 'Propiedad intelectual, datos, permisos y contingencias.'], ['Data room', 'Índice, versiones, responsables y brechas.']],
      method: [['Preparar', 'Perímetro, cronograma y requerimientos.'], ['Revisar', 'Documentos y brechas.'], ['Remediar', 'Prioridades antes de la revisión.'], ['Organizar', 'Data room y narrativa.'], ['Acompañar', 'Preguntas y decisiones dentro del alcance.']],
      deliverables: [['Mapa de brechas', 'Hallazgo, impacto y prioridad.'], ['Plan de remediación', 'Acciones, responsables y fechas.'], ['Arquitectura de gobierno', 'Cap table, órganos y materias reservadas.'], ['Índice de data room', 'Documentos, versiones y contingencias.']],
      requirements: [['Objetivo de inversión', 'Monto, etapa, tipo de inversionista y cronograma.'], ['Documentación corporativa', 'Cap table, estatutos, acuerdos y actas.'], ['Contratos y activos', 'Relaciones materiales e intangibles.'], ['Equipo disponible', 'Fundadores, finanzas, operación y tecnología.']],
      limits: ['No incluye valoración, modelación financiera ni captación de inversionistas.', 'No garantiza inversión ni cierre de la transacción.', 'Tributación, competencia y negociación integral pueden exigir especialistas.', 'La remediación depende de decisiones, firmas y terceros.'],
      related: [['Servicio', 'Sociedades, Gobierno e Inversión', 'Negociación y estructuración a la medida.', '../servicios/sociedades-gobierno-inversion.html'], ['Producto', 'Activos Intangibles Protegidos', 'Cierre de brechas de titularidad.', 'activos-intangibles-protegidos.html'], ['Producto', 'Empresa Jurídicamente Organizada', 'Regularización previa o posterior.', 'empresa-juridicamente-organizada.html']],
    },
    'product-ai': {
      type: 'Producto jurídico', code: 'P05', title: 'Programa de Gobernanza de IA',
      summary: 'Implementación estructurada de inventario, clasificación de riesgo, política, roles, aprobación de casos, debida diligencia de proveedores y gestión de incidentes.',
      duration: '4 a 8 semanas', modality: 'Programa de implementación', audience: 'Empresas que usan o desarrollan inteligencia artificial',
      question: '¿La organización puede demostrar cómo controla los riesgos de sus casos de uso de inteligencia artificial?',
      situations: [['Uso no inventariado', 'Las áreas utilizan herramientas sin aprobación central.'], ['Proveedor crítico', 'La empresa depende de una solución que procesa datos o influye en decisiones.'], ['Desarrollo propio', 'Se necesita asignar responsabilidades y controles.'], ['Exigencia de cliente o junta', 'Un tercero solicita evidencia de gobernanza.']],
      scope: [['Inventario', 'Casos, responsables, proveedores, datos y usuarios.'], ['Riesgo', 'Clasificación y nivel de aprobación.'], ['Gobierno', 'Política, roles, excepciones y comité.'], ['Control', 'Proveedor, supervisión, incidentes y revisión.']],
      method: [['Descubrir', 'Inventario inicial.'], ['Clasificar', 'Criterios de riesgo.'], ['Diseñar', 'Política y roles.'], ['Implementar', 'Registros y checklists.'], ['Transferir', 'Capacitación y revisión.']],
      deliverables: [['Inventario de casos', 'Uso, finalidad, responsable y estado.'], ['Matriz de riesgo', 'Clasificación, control y aprobación.'], ['Política y procedimiento', 'Reglas, roles y excepciones.'], ['Kit de implementación', 'Checklist, registro e incidentes.']],
      requirements: [['Patrocinador', 'Dirección con capacidad de aprobar reglas.'], ['Equipo interdisciplinario', 'Tecnología, datos, seguridad, jurídico y operación.'], ['Lista de herramientas', 'Proveedores, pilotos y desarrollos.'], ['Casos prioritarios', 'Usos de mayor impacto o escala.']],
      limits: ['No es auditoría técnica ni certificación algorítmica.', 'No garantiza ausencia de sesgos, errores o incidentes.', 'Casos de alto impacto requieren evaluación ampliada.', 'La gobernanza debe mantenerse después del proyecto.'],
      related: [['Servicio', 'Tecnología e Inteligencia Artificial', 'Acompañamiento a la medida y casos complejos.', '../servicios/tecnologia-inteligencia-artificial.html'], ['Producto', 'Protección de Datos y Consumidor', 'Procesos relacionados con datos y usuarios.', 'proteccion-datos-consumidor.html'], ['Servicio', 'Legal Operations', 'Flujos, aprobaciones y evidencia.', '../servicios/legal-operations.html']],
    },
    'product-regulated': {
      type: 'Producto jurídico', code: 'P06', title: 'Proyecto Regulado Estructurado',
      summary: 'Paquete de viabilidad para ordenar régimen, autoridades, actores, permisos, contratos, condiciones precedentes y secuencia de ejecución de un proyecto delimitado.',
      duration: '3 a 8 semanas', modality: 'Proyecto de viabilidad', audience: 'Promotores y aliados de proyectos regulados',
      question: '¿Qué condiciona la viabilidad jurídica y qué debe ocurrir antes de contratar, invertir u operar?',
      situations: [['Proyecto en etapa temprana', 'Debe definirse si el modelo puede avanzar.'], ['Inversión condicionada', 'El capital depende de permisos o contratos.'], ['Múltiples actores', 'Roles y responsabilidades no están claros.'], ['Ruta regulatoria incierta', 'No existe secuencia común de habilitaciones.']],
      scope: [['Modelo', 'Actividad, territorio y operación.'], ['Régimen', 'Normas, autoridades y restricciones.'], ['Actores', 'Funciones, riesgos y contraprestaciones.'], ['Ruta', 'Permisos, contratos y condiciones.']],
      method: [['Modelar', 'Descripción funcional.'], ['Calificar', 'Régimen y autoridad.'], ['Mapear', 'Actores y riesgos.'], ['Estructurar', 'Contratos y condiciones.'], ['Programar', 'Hoja de ruta.']],
      deliverables: [['Mapa normativo', 'Regímenes y autoridades.'], ['Matriz de actores', 'Funciones y responsabilidades.'], ['Matriz de permisos', 'Secuencia y evidencia.'], ['Hoja de ruta', 'Hitos y condiciones de avance.']],
      requirements: [['Descripción técnica', 'Proceso, capacidad y localización.'], ['Modelo económico', 'Ingresos, costos y relaciones.'], ['Actores', 'Promotores, operadores y autoridades.'], ['Estudios', 'Documentos técnicos disponibles.']],
      limits: ['No sustituye estudios técnicos o ambientales.', 'No garantiza permisos ni financiación.', 'Trámites y representación se contratan aparte.', 'Cambios del proyecto pueden exigir recalificación.'],
      related: [['Servicio', 'Proyectos Regulados', 'Análisis a la medida y acompañamiento extendido.', '../servicios/proyectos-regulados.html'], ['Servicio', 'Contratación Estratégica', 'Instrumentación de alianzas y operación.', '../servicios/contratacion-estrategica.html'], ['Plan', 'Gestión Jurídica Regulatoria', 'Seguimiento recurrente.', '../index.html#planes']],
    },
    'product-contract-system': {
      type: 'Producto jurídico', code: 'P07', title: 'Sistema Contractual Empresarial',
      summary: 'Transformación focal para pasar de contratos aislados a un sistema de solicitud, aprobación, modelos, playbooks, obligaciones, renovaciones y métricas.',
      duration: '6 a 10 semanas', modality: 'Proyecto de transformación', audience: 'Empresas con volumen contractual recurrente',
      question: '¿La empresa sabe qué firma, quién aprueba, qué debe administrar y cuándo debe actuar?',
      situations: [['Modelos múltiples', 'Cada área usa documentos distintos o desactualizados.'], ['Negociación lenta', 'No existen posiciones preaprobadas ni criterios de escalamiento.'], ['Obligaciones invisibles', 'Renovaciones, garantías y preavisos se descubren tarde.'], ['Canales dispersos', 'Las solicitudes no tienen estado ni expediente.']],
      scope: [['Demanda', 'Tipos, usuarios, volumen y prioridad.'], ['Modelos', 'Plantillas, cláusulas y anexos aprobados.'], ['Flujo', 'Solicitud, revisión, aprobación, firma y archivo.'], ['Administración', 'Obligaciones, renovaciones, evidencia y métricas.']],
      method: [['Diagnosticar', 'Demanda y fricción.'], ['Diseñar', 'Taxonomía y flujo.'], ['Construir', 'Modelos y playbook.'], ['Implementar', 'Piloto y capacitación.'], ['Medir', 'Indicadores y mejora.']],
      deliverables: [['Matriz contractual', 'Tipos, responsables y estado.'], ['Playbook', 'Posiciones, alternativas y aprobaciones.'], ['Biblioteca de modelos', 'Documentos y versiones.'], ['Flujo y obligaciones', 'Etapas, SLA y registros.']],
      requirements: [['Muestra contractual', 'Contratos representativos.'], ['Usuarios clave', 'Comercial, compras, operación y jurídico.'], ['Políticas de aprobación', 'Autoridad y umbrales.'], ['Herramientas disponibles', 'Repositorios, firma y sistemas.']],
      limits: ['La revisión histórica masiva se dimensiona aparte.', 'Negociaciones extraordinarias no están incluidas.', 'Integraciones requieren alcance técnico.', 'La adopción depende de gobierno y disciplina interna.'],
      related: [['Servicio', 'Contratación Estratégica', 'Negociaciones y contratos materiales.', '../servicios/contratacion-estrategica.html'], ['Servicio', 'Legal Operations', 'Transformación integral de la función jurídica.', '../servicios/legal-operations.html'], ['Plan', 'Gestión Contractual Continua', 'Operación recurrente del sistema.', '../index.html#planes']],
    },
    'product-data-consumer': {
      type: 'Producto jurídico', code: 'P08', title: 'Programa de Protección de Datos y Consumidor',
      summary: 'Programa para convertir políticas formales en inventarios, procedimientos, cláusulas, canales, responsables, evidencias y respuesta consistente a titulares y consumidores.',
      duration: '6 a 10 semanas', modality: 'Programa de implementación', audience: 'Empresas que tratan datos o venden bienes y servicios',
      question: '¿La empresa puede demostrar cómo recoge datos, informa condiciones, atiende reclamos y corrige incidentes?',
      situations: [['Políticas sin proceso', 'Existen documentos, pero no responsables o evidencia.'], ['Nuevos canales digitales', 'Se amplían formularios, comercio, marketing o proveedores.'], ['Reclamos inconsistentes', 'No existe procedimiento común para titulares o consumidores.'], ['Proveedores con acceso', 'Terceros procesan datos o intervienen en la experiencia del cliente.']],
      scope: [['Inventario', 'Datos, finalidades, canales, sistemas y responsables.'], ['Información', 'Políticas, avisos, términos y autorizaciones.'], ['Operación', 'Consultas, reclamos, garantías e incidentes.'], ['Terceros', 'Contratos, transferencias, encargos y evidencia.']],
      method: [['Levantar', 'Tratamientos, productos y canales.'], ['Calificar', 'Riesgo y brechas.'], ['Diseñar', 'Documentos y procedimientos.'], ['Implementar', 'Roles, registros y capacitación.'], ['Verificar', 'Pruebas de operación y mejora.']],
      deliverables: [['Inventario de tratamientos', 'Finalidad, base, dato, responsable y sistema.'], ['Paquete documental', 'Políticas, avisos, cláusulas y términos.'], ['Procedimientos', 'Titulares, garantías, reclamos e incidentes.'], ['Plan de capacitación', 'Roles, evidencias y actualización.']],
      requirements: [['Mapa de canales', 'Web, formularios, ventas y soporte.'], ['Sistemas y proveedores', 'Accesos, almacenamiento y terceros.'], ['Productos y condiciones', 'Oferta, garantías y comunicaciones.'], ['Responsables internos', 'Datos, servicio, tecnología y comercial.']],
      limits: ['No incluye pruebas técnicas de seguridad.', 'Investigaciones, litigios y sanciones se separan.', 'Transferencias internacionales requieren análisis específico.', 'El cumplimiento depende de operación y actualización continua.'],
      related: [['Servicio', 'Legal Operations', 'Procesos, roles y evidencia operativa.', '../servicios/legal-operations.html'], ['Servicio', 'Tecnología e Inteligencia Artificial', 'Datos, proveedores y casos automatizados.', '../servicios/tecnologia-inteligencia-artificial.html'], ['Documento', 'Autorización y aviso de datos', 'Documento guiado para necesidades delimitadas.', '../demo.html#documentos']],
    },
  };

  const create = (tag, className, text) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined) element.textContent = text;
    return element;
  };

  const appendCards = (parent, items, className, prefix) => {
    const grid = create('div', `${className}-grid`);
    items.forEach(([title, description], index) => {
      const card = create('article', `${className}-card`);
      card.append(create('span', '', `${String(index + 1).padStart(2, '0')} · ${prefix}`), create('h3', '', title), create('p', '', description));
      grid.append(card);
    });
    parent.append(grid);
  };

  const section = (eyebrow, title, description, className = '') => {
    const node = create('section', `detail-section ${className}`.trim());
    const container = create('div', 'container');
    const heading = create('div', 'detail-heading');
    heading.append(create('p', 'eyebrow', eyebrow), create('h2', '', title));
    if (description) heading.append(create('p', '', description));
    container.append(heading);
    node.append(container);
    return { node, container };
  };

  const render = (entry) => {
    const hero = document.getElementById('detail-hero-content');
    const page = document.getElementById('detail-page');
    if (!hero || !page) return;

    const copy = create('div');
    copy.append(create('p', 'detail-eyebrow', `${entry.type.toUpperCase()} · ${entry.code}`), create('h1', '', entry.title), create('p', 'summary', entry.summary));
    const actions = create('div', 'detail-cta-row');
    const contact = create('a', 'btn btn-gold', 'Presentar esta necesidad →');
    contact.href = '#contacto';
    const back = create('a', 'btn btn-outline-light', 'Volver al portafolio');
    back.href = entry.type === 'Servicio profesional' ? '../index.html#servicios' : '../index.html#productos';
    actions.append(contact, back);
    copy.append(actions);

    const meta = create('div', 'detail-meta');
    [['Tipo', entry.type], ['Horizonte', entry.duration], ['Modalidad', entry.modality], ['Dirigido a', entry.audience]].forEach(([label, value]) => {
      const item = create('article');
      item.append(create('span', '', label), create('strong', '', value));
      meta.append(item);
    });
    hero.append(copy, meta);

    const questionSection = section('PREGUNTA EJECUTIVA', 'La decisión que organiza el alcance.');
    const question = create('div', 'executive-question');
    question.append(create('span', '', 'PREGUNTA CENTRAL'), create('p', '', entry.question));
    questionSection.container.append(question);
    page.append(questionSection.node);

    const situationsSection = section('CUÁNDO PUEDE SER ÚTIL', 'Situaciones que justifican evaluar esta solución.', 'La calificación definitiva depende de hechos, documentos, actores, urgencia y especialidades aplicables.', 'soft');
    appendCards(situationsSection.container, entry.situations, 'situation', 'SITUACIÓN');
    page.append(situationsSection.node);

    const scopeSection = section('ALCANCE ORIENTATIVO', 'Qué frentes puede comprender.', 'La propuesta final define expresamente el perímetro, la profundidad, las revisiones y las exclusiones.');
    appendCards(scopeSection.container, entry.scope, 'scope', 'FRENTE');
    page.append(scopeSection.node);

    const methodSection = section('MÉTODO DE TRABAJO', 'Una secuencia que evita documentos prematuros.', 'El orden puede adaptarse al asunto, pero siempre debe conservar comprensión, calificación, estructuración, implementación y cierre.', 'ivory');
    const method = create('ol', 'method-list');
    entry.method.forEach(([title, description], index) => {
      const item = create('li');
      item.append(create('b', '', String(index + 1).padStart(2, '0')), create('strong', '', title), create('span', '', description));
      method.append(item);
    });
    methodSection.container.append(method);
    page.append(methodSection.node);

    const deliverablesSection = section('ENTREGABLES', 'Qué puede recibir la empresa.', 'Los formatos se ajustan al alcance y deben indicar supuestos, fuentes, responsables, límites y condiciones de actualización.');
    appendCards(deliverablesSection.container, entry.deliverables, 'deliverable', 'SALIDA');
    page.append(deliverablesSection.node);

    const requirementsSection = section('INFORMACIÓN Y PARTICIPACIÓN', 'Qué se requiere para trabajar con rigor.', 'La falta de información o de responsables puede modificar cronograma, profundidad y conclusiones.', 'soft');
    appendCards(requirementsSection.container, entry.requirements, 'requirement', 'REQUISITO');
    page.append(requirementsSection.node);

    const limitsSection = create('section', 'detail-section');
    const limitsContainer = create('div', 'container limits-layout');
    const limitsIntro = create('div', 'limits-intro');
    limitsIntro.append(create('p', 'detail-eyebrow', 'LÍMITES Y EXCLUSIONES'), create('h2', '', 'Claridad sobre lo que esta solución no promete.'), create('p', '', 'El rigor también exige separar decisiones propias, especialidades externas y resultados que dependen de autoridades o terceros.'));
    const limits = create('ul', 'limits-list');
    entry.limits.forEach((item) => limits.append(create('li', '', item)));
    limitsContainer.append(limitsIntro, limits);
    limitsSection.append(limitsContainer);
    page.append(limitsSection);

    const relatedSection = section('SOLUCIONES RELACIONADAS', 'Cómo puede conectarse con el resto del portafolio.', '', 'ivory');
    const relatedGrid = create('div', 'related-grid');
    entry.related.forEach(([label, title, description, url]) => {
      const card = create('article', 'related-card');
      const link = create('a', '', 'Explorar →');
      link.href = url;
      card.append(create('span', '', label), create('strong', '', title), create('p', '', description), link);
      relatedGrid.append(card);
    });
    relatedSection.container.append(relatedGrid);
    page.append(relatedSection.node);

    const contactSection = create('section', 'detail-section detail-contact');
    contactSection.id = 'contacto';
    const contactContainer = create('div', 'container detail-contact-grid');
    const contactCopy = create('div');
    contactCopy.append(create('p', 'detail-eyebrow', 'SIGUIENTE PASO'), create('h2', '', 'Definamos si esta es la solución adecuada para su necesidad.'), create('p', '', 'La primera conversación permite comprender la decisión, la urgencia, los actores, la evidencia y el resultado esperado. No envíe todavía información confidencial ni documentos sensibles.'));
    const contactPanel = create('div', 'detail-contact-panel');
    contactPanel.append(create('strong', '', entry.title), create('span', '', `${entry.type} · ${entry.duration}`));
    const whatsapp = create('a', 'btn btn-gold', 'Conversar por WhatsApp →');
    whatsapp.href = `https://wa.me/${WHATSAPP}?text=${encodeURIComponent(`Hola, revisé la ficha de ${entry.title} en Meridiano Legal y quiero presentar una necesidad relacionada.`)}`;
    whatsapp.target = '_blank';
    whatsapp.rel = 'noopener noreferrer';
    const general = create('a', 'btn btn-outline-light', 'Formulario general');
    general.href = '../index.html#contacto';
    const actionRow = create('div', 'detail-cta-row');
    actionRow.append(whatsapp, general);
    contactPanel.append(actionRow);
    contactContainer.append(contactCopy, contactPanel);
    contactSection.append(contactContainer);
    page.append(contactSection);
  };

  const id = document.body.dataset.catalogId;
  const entry = entries[id];
  if (!entry) {
    const page = document.getElementById('detail-page');
    if (page) page.textContent = 'No fue posible cargar esta ficha.';
    return;
  }
  render(entry);

  const menu = document.querySelector('.detail-menu');
  const nav = document.querySelector('.detail-nav');
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav?.classList.toggle('open', open);
  });
  nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    menu?.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
  }));

  document.querySelector('[data-top]')?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
