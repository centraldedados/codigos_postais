scrape:
	. `pwd`/.env/bin/activate; python3 download.py
	mv ~/Downloads/todos_cp.zip ./todos_cp.zip
	unzip todos_cp.zip todos_cp.txt
	rm -f todos_cp.zip
	# converter para utf-8 e remover line endings de DOS
	iconv -f ISO-8859-15 -t utf-8 todos_cp.txt | sed 's/^M//' > todos_cp.csv
	rm -f todos_cp.txt
	# adicionar cabeçalho e normalizar com o csvclean
	. `pwd`/.env/bin/activate; cat header.txt todos_cp.csv | csvclean -d ";"
	mv stdin_out.csv codigos.csv
	rm -f todos_cp.csv
	mv -f codigos.csv ../data/codigos_postais.csv

install:
	virtualenv .env --python=/usr/bin/python3 --no-site-packages --distribute --prompt=\(codpostais\)
	. `pwd`/.env/bin/activate; pip install -r requirements.txt
	@echo "--------------------------------------------------------------------------------------------"
	@echo ""
	@echo "Tudo instalado!"
	@echo "Agora, copia o credenciais.sample.ini para credenciais.ini:"
	@echo "    cp credenciais.sample.ini credenciais.ini"
	@echo ""
	@echo "E edita o ficheiro com o teu username e password no CTT.pt."
	@echo "Depois, é só correr:"
	@echo "    make scrape"
	@echo ""

deploy:
	git add ../data/codigos_postais.csv
	git commit -m "Atualização automática"
	git push origin master
