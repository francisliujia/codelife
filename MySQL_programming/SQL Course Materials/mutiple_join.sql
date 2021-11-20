use sql_invoicing;
select 
	p.date,
    p.amount,
    p.invoice_id,
    c.name,
    pm.name as 'payment method'

from payments p
join clients c
	on c.client_id = p.client_id
join payment_methods pm
	on p.payment_method = pm.payment_method_id