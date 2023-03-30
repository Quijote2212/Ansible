Sub CheckRedirects()
    Dim urls As Range
    Dim url As Range
    Dim http As Object
    
    ' Establece el rango de celdas que contiene las URLs
    Set urls = ActiveSheet.Range("A1:A" & ActiveSheet.Cells(Rows.Count, "A").End(xlUp).Row)
    
    ' Crea un objeto HTTP
    Set http = CreateObject("WinHttp.WinHttpRequest.5.1")
    
    ' Recorre cada URL en el rango y verifica si hay redirecciones
    For Each url In urls
        http.Open "GET", url.Value
        http.Send
        If http.Status >= 300 And http.Status < 400 Then
            MsgBox url.Value & " redirige a " & http.GetResponseHeader("Location")
        Else
            MsgBox url.Value & " no tiene redirecciones"
        End If
    Next url
End Sub
