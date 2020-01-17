import shutil
import os

diretorioOrigem = "."
diretorioDestino = "."
lista_arq = os.listdir(diretorioOrigem)
separador = "-"
for nomeArquivo in lista_arq:

	print(">>> ARQUIVO: {}".format(nomeArquivo) )
	if(separador in nomeArquivo):
		print("ESCOLHA A PARTE DE CLASSIFICACAO:")
		for i in range( len( nomeArquivo.split(separador) ) ):
			print("PARTE {} : '{}'".format( (i+1), nomeArquivo.split(separador)[i] ) )
		escolhido = int( input("PARTE: ") )	

		if (escolhido > 0):
			nomeDeClassificacao = nomeArquivo.split(separador)[escolhido - 1] 
			pastaDestino = nomeDeClassificacao.upper().strip()[0]
			saida = "{}/{}".format(diretorioDestino, pastaDestino)
			if( not os.path.isdir(saida)):
				os.makedirs(saida)

			print(shutil.move( "{}/{}".format(diretorioOrigem, nomeArquivo) ,  "{}/{}".format(saida, nomeArquivo) ) )

			print("Foi classificado")
		else:
			print("Não foi classificado")
	else:

		print("Não foi classificado")