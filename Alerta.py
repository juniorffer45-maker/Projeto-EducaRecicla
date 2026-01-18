def verificar_limite_categoria(self, categoria):
        """Verifica se os gastos de uma categoria específica excederam o limite planejado."""
        if categoria.limite_mensal is None:
            return f"Categoria {categoria.nome} não possui limite definido."
            
        total_gasto = sum(l.valor for l in self.lancamentos 
                          if isinstance(l, Despesa) and l.categoria == categoria)
        
        if total_gasto > categoria.limite_mensal:
            excedido = total_gasto - categoria.limite_mensal
            return f"⚠️ ALERTA: Limite excedido em '{categoria.nome}'! Gasto: R$ {total_gasto:.2f} | Limite: R$ {categoria.limite_mensal:.2f} (Excedeu: R$ {excedido:.2f})"
        
        return f"✅ Categoria '{categoria.nome}' está dentro do limite."