Flappy Bird 

¿Qué se implementó en este desarrollo?

Se añadieron las siguientes características principales:

Sistema de Pausa (PauseState): Se implementó un estado de pausa que permite detener la ejecución del juego con la tecla P, conservando intactos los estados del mundo y del pájaro al reanudar la partida.

Modos de Juego (Patrón Strategy): Se integró el patrón de diseño Strategy para soportar dos modalidades de juego fácilmente intercambiables.

Modo Normal: Conserva la jugabilidad clásica de Flappy Bird.
Modo Difícil: Aumenta la dificultad mediante características dinámicas. Permite movimiento horizontal libre para el pájaro, y una generación irregular de los troncos, con variaciones en las distancias y los espacios de apertura. Además, algunos troncos son móviles y se abren y cierran progresivamente, emitiendo sonido al chocar.
Power-Ups (Patrón Factory): Se introdujo un power-up aleatorio que otorga inmunidad temporal (efecto fantasma), permitiendo atravesar los troncos. Al recogerlo, cambia la música del juego, retornando a la normalidad al expirar el efecto.

Tambien fue añadida la tecla L para saltar. Se configuraron las colisiones con techo, piso y paredes. El pajaro al tocar algun limite muere, impidiendo algun bug en la movilidad. La inmunidad del power-up NO AFECTA la muerte por choque de estos limites.

La diferencia en Y entre un par de troncos es minimo 72px, seleccionado arbitrariamente. Con este minimo, se selecciona aletoriamente un multimplicador y del cual va a depender la distancia en X. El power-up dura 7.5 segundos activo. Los troncos que se cierran, duran 0.2 segundos cerrando/abriendo y duran 1.5 segundos abiertos y 0.5 segundos cerrado.
